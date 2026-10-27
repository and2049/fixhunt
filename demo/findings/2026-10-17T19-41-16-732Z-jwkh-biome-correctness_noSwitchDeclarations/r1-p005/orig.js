function f() {
  switch (x) {
    case 0:
      let y = 1;
      loop: {
        y++;
        break loop;
      }
      return y;
    default:
      return 0;
  }
}
x = 0;
console.log(f()); // 2
// Fix wraps case 0 in { ... } → label 'loop' is now block-scoped → still valid? 
// Actually, labels are function-scoped regardless of block — so this may NOT break.
// Need better example: label referenced from outside the case but inside switch
// Revised:
function f() {
  switch (x) {
    case 0:
      const y = 1;
      outer: {
        break outer;
      }
      return 1;
    case 1:
      break outer; // ← This breaks if case 0 is wrapped in block
      return 2;
  }
  return 0;
}
x = 0;
try { console.log(f()); } catch (e) { console.log(e.name + ': ' + e.message); }
x = 1;
try { console.log(f()); } catch (e) { console.log(e.name + ': ' + e.message); }
// Original: x=0 → returns 1; x=1 → breaks outer (from case 0) → returns nothing? Actually breaks to after switch → returns 0
// After fix: case 0 is wrapped → label 'outer' is not in scope for case 1 → ReferenceError
