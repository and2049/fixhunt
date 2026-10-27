// Hazard 4: Coercion in property access
const o = { '0': 'zero', '1': 'one', 2: 'two' };
let idx = 0;
// Rule fires on next line: const v = o[idx]; (idx is identifier, not literal)
// BUT we need a literal index for rule to fire - adjust:
const v = o[0]; // literal 0, v matches? no -> rule does NOT fire on v=o[0]
// Instead trigger on string literal match:
const k = '1';
const val = o[k]; // k is identifier -> no fire
// Final: use obj['0'] style with literal string that matches var name? impossible.
// Redesign: use obj.a where a is var name
const a = 5;
const obj = { a: 99 };
const a_val = obj.a; // YES: var name 'a_val' != prop 'a' -> NO FIRE
// Need var name == prop name:
const prop = 'a';
const obj2 = { a: 88 };
// const a = obj2.a; // var name 'a' == prop 'a' -> SHOULD FIRE
const a = obj2.a;
console.log('val:', a);
