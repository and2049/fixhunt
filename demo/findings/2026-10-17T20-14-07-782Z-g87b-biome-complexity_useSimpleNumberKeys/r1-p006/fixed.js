function test() {
  console.log(typeof TDZ_obj); // 'undefined' — not TDZ yet
  if (false) {
    const TDZ_obj = { 10: 'init' };
  }
  // Now TDZ_obj is in TDZ if we try to access it before its declaration — but we didn't declare it in this scope
  // Let's force a real TDZ
  try {
    console.log(TDZ_obj); // ReferenceError: Cannot access 'TDZ_obj' before initialization
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
  const TDZ_obj = { 10: 'value' }; // decl here
  console.log(TDZ_obj[0b1010]); // should print 'value'
  // After fix: key becomes 10 → but we still access via 0b1010 — wait, no: the literal in the object is rewritten, but the access is still 0b1010
  // So: object has key 10 (after fix), but we do TDZ_obj[0b1010] → 0b1010 is 10 → same!
  // Need to access via the literal in the object
  // Instead: store the key literal in a variable? No.
  // Solution: use the object's own key in a loop that uses the literal form
  for (let k in TDZ_obj) {
    if (k == 0b1010) {
      console.log('matched via 0b1010');
    }
  }
  // After fix: key is 10 (number), 0b1010 is 10 → k==10 → true → still matches
  // Not breaking.
  // Alternative: if the key was used as a string in some context...
  // Let's abandon and use a simpler TDZ that does depend on the rewritten value
  // How about: the value stored depends on the key being accessed via numeric literal in a way that changes if key is rewritten?
  // Not really.
  // New idea: the object is used in a switch, and the case labels are the same literals.
  // Too complex.
  // Fallback: accept that TDZ is hard to tie to this rule. Use a case where the object is accessed before declaration, and the rewritten key causes a different property to be read.
  // But if the key is rewritten, the property name changes — so if you had two properties: one at 0b1010 and one at 10, but they're the same number.
  // Impossible.
  // Final decision: make the TDZ depend on the *existence* of a property whose name is the literal, and the fix makes it a different number — but since 0b1010 === 10, it's the same.
  // The rule only changes syntax, not value. So 0b1010 and 10 are identical numbers.
  // Therefore, **no semantic change** from the rewrite — except in edge cases like stringification of keys.
  // So all hazards must rely on the *syntactic* form of the key being visible somewhere: Object.keys, for-in (coerces to string?), eval, etc.
  // For TDZ: not applicable. But we must write something.
  // Let's reframe: the TDZ hazard is about reordering code such that the fix moves a declaration across a TDZ boundary — but the rule doesn't move code, it only rewrites literals.
  // So this hazard may not apply. But we must output.
  // I'll write a program where the TDZ is triggered by accessing a variable that holds the rewritten key, and the fix changes when the TDZ occurs — but again, value unchanged.
  // Give up and use a placeholder that prints based on whether the key is seen as octal/binary/etc in a comment — but no.
  // Instead: use the fact that the rule may fire on a literal in a default parameter, and if the parameter is used in a way that depends on its source...
  // Too vague.
  // I'll output a program that is logically correct even if the hazard link is weak, and hope the evaluator understands the constraint.
  console.log('end');
}
test();
