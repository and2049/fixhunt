if (true) {
  function f() {
    return { 0b1010: 'block-scoped' };
  }
}
const obj = f();
console.log(obj[0b1010]); // Should print 'block-scoped'
// After fix: key becomes 10 → but 0b1010 is still 10 → obj[10] exists → same
// Not broken. Need the key to be accessed in a way that shows the original literal form.
// Solution: return the object and inspect its keys via a method that shows source
// Impossible in JS.
// Alternate: if the function is called multiple times and the object is mutated based on the key's lexical form? No.
// Final: use the object in a for-in loop and compare the key to the literal using == — which works because 10 == 0b1010
// Still not breaking.
// Accept that for this rule, semantic change only appears in stringification contexts.
// So for this hazard, we'll show that the function declaration is inside a block, and the object it returns has a key that, when stringified, differs.
console.log(Object.keys(obj)[0]); // prints '10' after fix, was '1_000'? No — for 0b1010, before and after: key is number 10 → Object.keys gives '10'
// Wait: before fix, the source was 0b1010, but the value is still the number 10. JS does not preserve the source of numeric literals in objects.
// There is **no way** to observe the original spelling of a numeric key in JS after object creation.
// Therefore, **this rule cannot change program semantics** — except in cases where the numeric literal appears in a context where its spelling is evaluated: like in eval, or in code generation where the object is used as a template.
// Hence, the only valid hazards are those involving:
// - eval(string containing the literal)
// - code generation that uses the object's structure to produce source
// - maybe JSON.stringify? No, it turns keys to strings — but 10 and 0b1010 both become '10'.
// - Object.keys: same.
// - ...
// Actually: none. The rule is *semantically inert* in standard JS.
// But the problem states it can alter semantics — so we must assume contexts like:
// - If the code is minified and the literal is used in a way that depends on token length (impossible)
// - Or if the literal is inside a comment? No.
// Given the constraints, I will produce programs where the rewritten literal is used in an `eval` string or in a string concatenation that is later eval'd, so that the *textual* form matters.
// Redo all programs with this insight.
