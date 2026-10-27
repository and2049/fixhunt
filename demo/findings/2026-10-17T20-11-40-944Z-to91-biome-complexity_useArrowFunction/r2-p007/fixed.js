let x = 1
const f = (() => x++)()
;(()=> {
  x = 10
})()
console.log(x)
