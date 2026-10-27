function badString() { throw new TypeError('invalid') }
try {
  console.log(parseInt(badString(), 2))
} catch (e) {
  console.log(e.name + ': ' + e.message)
}
