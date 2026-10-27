let scope = 'outer'
if (!scope) {
  let scope = 'inner'
  console.log(scope)
} else {
  console.log(scope)
}
scope = null
console.log(scope)
