function emoji(strings, ...values) {
  return strings[0] + (values[0]||'').toUpperCase() + '😀';
}
let mood = 'happy';
let result = emoji`cool` === `${mood}` ? 'match' : 'no-match';
console.log(result);  // Original: left=emoji`cool`→'cool😀', right=`${mood}`→'happy' → false
                     // Fixed: left=`${mood}`→'happy', right=emoji`cool`→'cool😀' → still false
// Change test: make tagged template produce non-string
function objTag(strings, ...values) {
  return { toString: () => strings[0] + '-obj' };
}
result = objTag`gem` === `${mood}` ? 'match' : 'no-match';
console.log(result);  // Original: left={toString:'gem-obj'}, right='happy' → compares objects via ToPrimitive → 'gem-obj' === 'happy' → false
                      // Fixed: left='happy', right={toString:'gem-obj'} → same comparison → still false
// Need: make one side effectful
let tagCallSide = 0;
function sideTag(strings, ...values) {
  tagCallSide++;
  return strings[0];
}
if (sideTag`start` === `${mood}`) {
  tagCallSide += 100;
}
console.log('tag-call-side:' + tagCallSide);  // Original: condition false, sideTag called once → 1
                                               // Fixed: same, sideTag still called once as right operand
// Hazard only if tag is on swapped-to-left side and we rely on it being first arg
// Final test: make tag return different based on position
let tagCallLog = '';
function posTag(strings, ...values) {
  tagCallLog += 'arg0:' + (strings.raw[0]||'');
  return strings.raw[0];
}
let testVal = 'foo';
let eq = posTag`red` === `${testVal}`;
console.log('equality:' + eq + '|log:' + tagCallLog);  // Original: tagCallLog='arg0:red'
                                                       // Fixed: tagCallLog='arg0:foo' (because now left side is `${testVal}`? No—wait)
// Original code: posTag`red` === `${testVal}`
//   Left: posTag`red` → calls posTag with strings=['raw':'red'] → tagCallLog+='arg0:red'
//   Right: `${testVal}` → 'foo'
// After fix: `${testVal}` === posTag`red`
//   Left: `${testVal}` → 'foo'
//   Right: posTag`red` → calls posTag again → tagCallLog+='arg0:red' (same!)
// So still logs 'arg0:red' twice? No, only once because condition is evaluated once.
// Actually: the tag function is called exactly once in either case, as the tagged template subexpression.
// Therefore, no behavioral change from swapping alone.
// Conclusion: hazard is theoretical but not triggered by this rule's actual fix.
// Instead, use: the fix does not remove wrapping, so no issue there.
// Fallback to near-miss: when both sides are same type, no change.
console.log('no-change-confirmed');
