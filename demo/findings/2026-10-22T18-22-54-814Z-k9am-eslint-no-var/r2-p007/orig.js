var x = 1
(function(){
  return x;
})()
// After fix: let x = 1
(function(){...})() still works, but if ASI breaks due to comment loss...
// We make it depend on comment-attached var
/* start */ var /* mid */ y = 2 /* end */
[3,4].forEach(v => console.log(v + y));
