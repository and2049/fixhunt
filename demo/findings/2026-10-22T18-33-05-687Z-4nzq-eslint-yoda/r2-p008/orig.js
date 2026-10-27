let x = 1
let y = 2
if (x < y) [].push.call(arguments, 1) // triggers yoda: x < y
console.log('no error')
let a = 1
let b = 2
if (a > b) (function(){ console.log('should not run') })()
console.log('no error')
