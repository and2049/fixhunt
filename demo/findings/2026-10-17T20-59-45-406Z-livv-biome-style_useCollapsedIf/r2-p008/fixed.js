// Hazard 1: comment between braces
let log = '';
if (true) { /* keep me */
  if (false) {
    log += 'inner';
  }
}
if (log === '') log = 'none';
console.log('log:', log);
