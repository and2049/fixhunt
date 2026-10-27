(function () {
  var a = 1
  (function () {
    console.log('IIFE executed:', a)
  })()
  return a
})()
