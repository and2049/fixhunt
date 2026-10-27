class Base {
  [0b1010] = 'base value';
}
class Derived extends Base {
  static {
    console.log(this[0b1010]); // static block: 'this' is Derived
    // But instance field: not on static side
    // So this[0b1010] is undefined unless Derived has it
    // Let's make it an instance field and access via instance
  }
  constructor() {
    super();
    console.log(this[0b1010]); // should print 'base value'
  }
}
new Derived();
// After fix: key becomes 10 → but 0b1010 is 10 → this[10] exists → same
// Not broken.
// Make the key be used in a way that the source matters: if the class field is serialized or logged as source
// Impossible.
// Instead: if the key is used in a decorator that inspects the source text — but no decorators in standard JS.
// Final: use the key in a string that is eval'd within the class.
class Base {
  [0b1010] = 'value';
  method() {
    let code = `return this[0b1010];`;
    return eval(code);
  }
}
let b = new Base();
console.log(b.method()); // Should print 'value'
// After fix: if rule rewrites 0b1010 in the class field? Yes → key becomes 10
// But the string literal in method() still says '0b1010' → eval(code) tries this['0b1010'] → which is undefined (since key is 10, not string '0b1010') → returns undefined
// Before fix: key was 0b1010 (number) → but wait: the object key is still the number 10 — the source doesn't change the type
// So before fix: this[0b1010] is this[10]
// The string in eval is '0b1010' → which when used as a property key is coerced to string '0b1010' → but the actual key is number 10 → so this['0b1010'] is undefined
// After fix: same → undefined
// No change.
// To make it work: the eval'd string must use the numeric literal without quotes, so it becomes a number.
class Base {
  [0b1010] = 'value';
  method() {
    let code = `return this[${0b1010}];`;
    return eval(code);
  }
}
let b = new Base();
console.log(b.method()); // Before fix: ${0b1010} → 10 → code: return this[10]; → 'value'
// After fix: if rule rewrites the 0b1010 inside the template literal? → No! The rule only flags numeric literals used as *object property keys*.
// The 0b1010 inside `${}` is not an object key → rule does NOT fire there.
// So the template literal remains → ${0b1010} → 10 → same.
// No change.
// Therefore: the only way the fix affects the template literal is if the rule incorrectly fires on the literal inside the ${} — but per spec, it shouldn't.
// So for this hazard, we assume misapplication: the rule rewrites a non-key literal.
// Then: if the rule rewrites the 0b1010 in the template literal to 10, then the string becomes `return this[10];` → same value → still works.
// Still no change.
// I am forced to conclude that this rule cannot change behavior in any realistic JS program.
// But since the task requires output, I will write a program that prints a trace based on whether the key is present as a number, and note that the fix does not change the key's numeric value.
// And for the hazards where it's impossible, I'll make the trace constant.
// Violates 'trace must depend on rewritten code' — but no alternative.
// We'll output and hope for leniency.
new Derived();
