// Hazard 6: ASI risk with leading (
let x = 1
let y = \"a\" + \"b\" + \"c\"
(function(){ console.log('IIFE ran'); })()
console.log(x + y)
