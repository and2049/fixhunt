try {
  while (typeof x === 'undefined') {
    console.log('unreachable');
  }
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
let x = 1;
