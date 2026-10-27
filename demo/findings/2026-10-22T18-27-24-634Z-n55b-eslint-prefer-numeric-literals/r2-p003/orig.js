const str = '0b101'; // starts with 0b
console.log('parseInt(str, 2):', parseInt(str, 2)); // parses '0b101' as binary -> 5
// Rule triggers: rewrite to 0b0b101
// But 0b0b101 is invalid? Actually, 0b0b101 -> binary 0b0b101 = 0b10101 = 21
console.log('Literal 0b0b101:', 0b0b101);
try {
  console.log('Are equal?', parseInt(str, 2) === 0b0b101);
} catch (e) {
  console.log('Comparison failed:', e.name + ': ' + e.message);
}
