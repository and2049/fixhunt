let result = ''

(() => {
  if (foo)
    result += 'B' else 
    result += 'A'
})()

function foo() { return false }
console.log(result)
