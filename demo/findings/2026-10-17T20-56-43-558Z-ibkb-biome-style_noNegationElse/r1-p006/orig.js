(() => {
  const obj = { prop: null };
  const log = [];
  // Hazard: !obj.prop reads as 'if missing' - clearer than !!obj.prop
  if (!obj.prop) { log.push('missing'); } else { log.push(obj.prop); }
  console.log(log.join('|')); // Should be 'missing'
  // After fix: condition becomes obj.prop -> null (falsy), so if block runs -> same output?
  // Wait: after fix, we swap blocks!
  // Original: if (!obj.prop) { A } else { B }
  // Fixed:    if (obj.prop) { B } else { A }
  // So now: if (null) -> false -> else runs -> A: 'missing'
  // Still same output. Need side effect.
  // Let's make else block have side effect
})();
// Redo with mutation
(() => {
  let val = 'start';
  const obj = { prop: null };
  if (!obj.prop) { val = 'if'; } else { val = 'else'; }
  console.log(val); // 'if'
  // After fix: if (obj.prop) { val = 'else'; } else { val = 'if'; } -> still 'if'
  // Need the condition to be truthy after fix to trigger else->if swap visibly
  // Use obj.prop = undefined initially, then change it
})();
// Final attempt: make condition depend on mutable state
(() => {
  let state = 0;
  const obj = { prop: () => state++ };
  // First eval: obj.prop() = 0 -> !0 = true -> if block
  // After fix: condition becomes obj.prop() -> 0 -> falsy -> else block
  // But we swap blocks too!
  // Original: if (!obj.prop()) { A } else { B }
  // Fixed:    if (obj.prop()) { B } else { A }
  // First call: state=0 -> obj.prop()=0 -> !0=true -> A runs
  // After fix: first call to obj.prop() in condition -> returns 0 -> falsy -> else runs -> A still?
  // We need to log which block ran
})();
// Correct version:
{"programs":[{"title":"Readability loss: intentional negation for null guard","hazard":"Rewritten condition may be harder to read, especially when negation guards against null/undefined.","expect_trigger":true,"code":"(() => {\n  let log = '';\n  const obj = { value: 42 };\n  // Hazard: negation makes intent clear: 'if not present'\n  if (!obj.value) { log = 'zero'; } else { log = obj.value.toString(); }\n  console.log(log); // '42'\n  // After fix: if (obj.value) { log = obj.value.toString(); } else { log = 'zero'; } -> still '42'\n  // No change. Need the negation to be semantically critical.\n  // Use case: guarding access where falsy means invalid\n}})]}
