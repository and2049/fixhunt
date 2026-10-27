"use strict";
let log = [];
(function(){ 
  var undefined = 42; // shadowing
  let x ;  // rule triggers: removes this line
  log.push(String(x));
})();

// After fix: x is undeclared -> ReferenceError
try {
  (function(){
    var undefined = 42;
    let x;          // autofixed version
    log.push(String(x));
  })();
} catch(e) {
  log.push(e.name + ': ' + e.message);
}

console.log(log.join(' | '));
