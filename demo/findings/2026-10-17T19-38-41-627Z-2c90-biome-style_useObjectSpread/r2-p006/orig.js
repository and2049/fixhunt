function getObj() { return {x: 1} }
function test() {
  return Object.assign({}, getObj());
}
try { test() } catch(e) {
  console.log(e.stack.split('\n')[1].trim())
}
