let input = null
let radix = undefined
try {
  console.log(parseInt(input?.trim(), radix ?? 10))
} catch (e) {
  console.log(e.name + ': ' + e.message)
}
input = '11'
radix = 2
console.log(parseInt(input?.trim(), radix ?? 10))
