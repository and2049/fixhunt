let obj = {a: 1}
let {a: a} = obj
(function(){ console.log('IIFE ran, a =', a) })()
console.log('after')
