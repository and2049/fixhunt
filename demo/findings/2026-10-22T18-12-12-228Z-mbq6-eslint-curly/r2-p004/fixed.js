function outer() {
  if (true)
    {return inner()}
}
function inner() {
  try { throw new Error() } catch (e) {
    let depth = 0
    let f = arguments.callee.caller
    while (f && f !== outer) { depth++; f = f.caller }
    console.log(depth)
  }
}
outer()
