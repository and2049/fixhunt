let i = 0;
function logAndInc() {
  console.log('side', i);
  return i++;
}
if ((logAndInc(), !!logAndInc()) < 10) {
  console.log('pass');
} else {
  console.log('fail', i);
}
