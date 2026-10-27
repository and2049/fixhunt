let x = 1
;
(function(){ return 5; })()
console.log('first:', x)
x = 0
;
(function(){ return 6; })()
console.log('second:', x)
