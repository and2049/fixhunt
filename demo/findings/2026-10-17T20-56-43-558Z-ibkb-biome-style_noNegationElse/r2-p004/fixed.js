let scope = 'outer'
if (scope) {
  console.log(scope)
} else {
  let scope = 'inner'
  console.log(scope)
}
scope = null
console.log(scope)
