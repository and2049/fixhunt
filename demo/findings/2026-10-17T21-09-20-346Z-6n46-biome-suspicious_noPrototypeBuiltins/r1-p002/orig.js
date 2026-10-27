if (typeof foo === 'undefined') {
  try {
    console.log(foo.hasOwnProperty('x'));
  } catch (e) {
    console.log(e.name, e.message);
  }
}
var foo = { x: 1 };
