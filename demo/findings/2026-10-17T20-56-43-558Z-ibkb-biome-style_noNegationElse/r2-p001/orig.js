let result = ''

(() => {
  if (!foo)
    result += 'A'
  else
    result += 'B'
})()

function foo() { return false }
console.log(result)
