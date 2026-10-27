function tag(strings, ...values) {
  return strings.raw[0] + '-' + (values[0] || 'empty');
}
let value = 'hello';
let result = tag`red` === tag`${value}` ? 'equal' : 'not-equal';
console.log(result);  // Original: 'red-' + 'hello', Fixed would be: tag`${value}` === tag`red` → same comparison
// But if we had: tag`red` === ${value}  ---  this doesn't fire rule because RHS is not template literal
// Adjust: make it tag`red` === tag`${value}`  ---  still symmetric
// Need asymmetric: tagged vs untagged
function id(s) { return s; }
result = id`red` === `${value}` ? 'equal' : 'not-equal';
console.log(result);  // Rule fires on: id`red` === `${value}`  → swap to: `${value}` === id`red`
// Original: left=id`red` (returns 'red'), right=`${value}` (string 'hello') → 'red' === 'hello' → false
// Fixed: left=`${value}` ('hello'), right=id`red` (tag function called with ['red'], returns 'red') → 'hello' === 'red' → false
// Still same? Yes, because both are string comparisons.
// Real hazard: if tag has side effect
let callLog = '';
function sideTag(strings, ...values) {
  callLog += 'tag-called:' + (strings.raw[0]||'');
  return strings.raw[0];
}
result = sideTag`red` === `${value}` ? 'equal' : 'not-equal';
console.log(result + '|' + callLog);
