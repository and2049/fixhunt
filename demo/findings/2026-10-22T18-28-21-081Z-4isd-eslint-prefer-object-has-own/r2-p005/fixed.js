for (var i = 0; i < 2; i++) {
  var o = {a: i};
  if (Object.hasOwn(o, 'a')) {
    console.log('loop', i, 'has a');
  }
}
console.log('o after loop:', typeof o);
if (Object.hasOwn(o, 'a')) {
  console.log('o has a');
} else {
  console.log('o does not have a');
}
