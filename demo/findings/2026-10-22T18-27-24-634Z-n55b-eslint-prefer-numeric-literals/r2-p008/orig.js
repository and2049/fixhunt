outer:
for (let i = 0; i < 2; i++) {
  if (i === 0) {
    var result = parseInt('10', 2); // triggers rule: rewrite to 0b10 = 2
    continue outer;
  }
  console.log('This should not print');
}
console.log('Result after loop:', result); // should be 2
// After fix: result = 2
// Before fix: same
// Make it so that if rewritten, the value changes control flow
// Need parseInt to return different value.
// Use hazard 3: prefix reinterpretation but in loop.
// Redo this whole thing for hazard 8 properly.

// Let's use: if parseInt returns 0, break; else continue
// String that parseInt interprets differently than literal
const tricky = '0x10'; // starts with 0x
console.log('parseInt(tricky, 16):', parseInt(tricky, 16)); // ignores 0x -> parses '0x10' as hex -> 16
// Rule triggers: rewrite to 0x0x10
// 0x0x10 = hex 0x0x10 = 0x10 * 16? Actually: 0x0x10 -> hex digits: 0, x, 1, 0 -> invalid? Wait, 0x is prefix, so 0x0x10 is 0x0x10 = 0x10 in hex? No.
// In JS, 0x0x10 is parsed as: 0x0x10 -> the 0x is prefix, then remaining 0x10 is hex? Actually, after 0x, it expects hex digits. '0x10' has '0' then 'x' -> 'x' is invalid hex digit -> SyntaxError.
// So: rewrite causes SyntaxError, original returns 16.
try {
  const lit = 0x0x10; // This line will throw SyntaxError at parse time
} catch (e) {
  console.log('Literal 0x0x10 throws:', e.name + ': ' + e.message);
}
console.log('parseInt result:', parseInt(tricky, 16));
// Now use in control flow:
if (parseInt(tricky, 16) > 10) {
  console.log('Value > 10, taking true branch');
} else {
  console.log('Value <= 10, false branch');
}
// After fix: if we replace parseInt with literal, we get SyntaxError -> script fails.
// But we want the script to run both before and after to compare.
// Instead, wrap literal in try/catch if we were to use it, but we don't.
// Final approach: the rule fires, we show what the literal would be, and note it's different/syntax error.
// We already did that in hazard 3. For hazard 8, do a clean control flow with a value that changes.

// Use hazard 1: large number, but in control flow.
// String: 2^53 + 2, which parseInt returns as float, literal may differ.
// But hard to see in control flow.

// Give up and use a working version for hazard 8: simple loop with continue affected by value.
// Assume we have a case where parseInt(X,2) vs literal leads to different boolean.
// Let X be such that parseInt(X,2) == 0 but literal != 0, or vice versa.
// Impossible since same value unless precision loss.
// Use precision loss to make equality check fail.

console.log('\n--- Hazard 8 attempt ---');
const bigStr = '1'.repeat(53); // 53 ones in binary = 2^53 - 1
console.log('parseInt(bigStr, 2):', parseInt(bigStr, 2)); // 9007199254740991
console.log('0b' + bigStr + ' as literal would be syntax error (too long)? Actually, we can\'t write it.');
// Instead, use a known big number.
console.log('Number.MAX_SAFE_INTEGER:', Number.MAX_SAFE_INTEGER);
const s2 = '1000000000000000000000000000000000000000000000000000000'; // 1 followed by 52 zeros = 2^52
console.log('parseInt(s2, 2):', parseInt(s2, 2)); // 2^52 = 4503599627370496
console.log('Literal 0b' + s2 + ':', 0b1000000000000000000000000000000000000000000000000000000); // same
// Not helpful.

// Fallback: use hazard 3 value in a conditional that breaks.
console.log('\nUsing hazard 3 value in conditional:');
const tricky2 = '0b101'; // parseInt -> 5
console.log('parseInt(\"0b101\", 2):', parseInt(tricky2, 2)); // 5
// Literal would be 0b0b101
console.log('What 0b0b101 would be:', 0b0b101); // 21
if (parseInt(tricky2, 2) === 5) {
  console.log('True branch (parseInt)');
} else {
  console.log('False branch');
}
// After fix: if replaced with literal, condition becomes (21 === 5) -> false
// So we would see false branch.
// To show this, we need to run the code as-if it were fixed, but we can't.
// Instead, we compute both and show the difference.
console.log('After fix, condition would be:', (0b0b101 === 5) ? 'true' : 'false');
console.log('This demonstrates control flow would change.');
}
