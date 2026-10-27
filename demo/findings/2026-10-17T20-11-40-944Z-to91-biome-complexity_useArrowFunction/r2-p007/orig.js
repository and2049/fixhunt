let x = 1
const f = function() {
  return x++
}()
;(function(){
  x = 10
})()
console.log(x)
