function processFlag(mode) {
  const log = [];
  if (mode === 'fast') {         // fast path
    return 100;                  // <- value 100
  }                              
                           // <- Hazard: comment-rich else
    /* step 1 */                 // Comment on statement
    log.push('start');           // inline comment
    /* step 2 */                 
    mode.toUpperCase();          // side effect
    return log.join('|');        
  
  log.push('end');               // Should not execute
  return log.length;
}
console.log(processFlag('fast'));
console.log(processFlag('slow'));
