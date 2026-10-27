function getObj() { return {x: 1} }
function test() {
  return ({...getObj(),});
}
try { test() } catch(e) {
  console.log(e.stack.split('\n')[1].trim())
}
