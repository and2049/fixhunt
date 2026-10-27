let x = 1
for (let i = 0; i < 1; i++) {
  x++
}
(x => { console.log('called', x); })(5)
// Without ASI fix: x++ then continue then (x=>...) call is part of expr? 
// Actually: after fix, we have x++; continue; then (x=>..)(5) -> ASI sees ; before (
// So it's fine. But if we had:
let y = 2
for (let j = 0; j < 1; j++) { y++; }
[1,2].forEach(v=>{console.log('arr',v)})
// Here: y++; continue; [1,2]... -> without semicolon, [ is interpreted as indexing? 
// y++ ; continue [1,2]... -> SyntaxError
// So we need to show that after fix, ASI breaks.
try {
  let z = 0
  for (let k = 0; k < 1; k++) { z++; }
  [z].forEach(v=>console.log('ASI safe:', v))
} catch(e) {
  console.error(e.name, e.message)
}
