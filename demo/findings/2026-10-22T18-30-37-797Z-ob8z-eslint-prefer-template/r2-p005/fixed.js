for (var i = 0; i < 2; i++) {
  var msg = `i:${  i}`;
  console.log(msg);
  if (i === 0) var msg = 'redeclared'; // hoisted, but block-scoped effect
}
console.log('final i:', i);
