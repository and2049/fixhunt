let x = 1
{}
[1,2,3].forEach(v => console.log(v))
// Before: {} is parsed as empty block, then [1...] is array literal -> prints 1,2,3
// After fix: remove {} -> now: let x = 1
// [1,2,3].forEach(...) -> ASI: tries to parse as 1[1,2,3] -> TypeError
try {
  let x = 1
[1,2,3].forEach(v => console.log(v))
} catch(e) {
  console.log('Error:', e.name + ': ' + e.message)
}
