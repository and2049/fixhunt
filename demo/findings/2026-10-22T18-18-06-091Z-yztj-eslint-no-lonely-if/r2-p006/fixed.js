let a = 0;
if (a) {/* unreachable */} else { // this comment should stay
  if (a === 0) console.log('zero');
}
// Output should show comment proximity affects nothing, but we log to see if
// formatting change alters execution (it shouldn't, but we check)
console.log('done');
