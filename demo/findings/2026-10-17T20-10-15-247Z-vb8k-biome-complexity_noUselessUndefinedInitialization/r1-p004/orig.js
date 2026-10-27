let throws = false;
function sideEffect() {
  if (throws) throw new Error('side effect');
  return 'ok';
}

try {
  let x = sideEffect(); // Not undefined init → rule silent
  console.log('Assigned:', x);
} catch (e) {
  console.log('Caught:', e.name, e.message);
}

throws = true;
try {
  let y = sideEffect();
  console.log('Assigned:', y);
} catch (e) {
  console.log('Caught:', e.name, e.message);
}
