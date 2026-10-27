let log = [];
(function(){ 
  var undefined = 42; // shadowing
  let x = undefined;  // rule triggers: removes this line
  log.push(String(x));
})();
try {
} catch(e) {
}
console.log(log.join(' | '));
