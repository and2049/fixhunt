if (typeof foo === 'undefined') {
  try {
    console.log(Object.hasOwn(foo, 'x'));
  } catch (e) {
    console.log(e.name, e.message);
  }
}
var foo = { x: 1 };
