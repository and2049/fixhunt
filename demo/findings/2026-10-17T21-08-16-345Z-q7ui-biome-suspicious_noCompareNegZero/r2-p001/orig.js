function getX() { throw new Error('bad'); }
try {
  if (getX() == -0) {
    console.log('equal');
  }
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
