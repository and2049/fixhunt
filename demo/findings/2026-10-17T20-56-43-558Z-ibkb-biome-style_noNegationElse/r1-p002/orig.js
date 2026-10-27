(function(){
  var x = 99;
  // Hazard: outer 'x' shadows inner if swapped
  if (!var x = 5) { /* unreachable */ } else { /* uses outer x */ return x; }
  // This line won't run due to syntax error above, but we adjust:
})();
// Let's fix syntax by moving decl to init-part with comma
(() => {
  var x = 99;
  // Hazard: if condition declares var, which is hoisted
  if (! (x = 5, false) ) { /* if */ } else { log.push(x); }
  var log = [];
  if (! (x = 5, false) ) { log.push('if'); } else { log.push(x); }
  console.log(log.join('|')); // Should be 5, not 99
})();
