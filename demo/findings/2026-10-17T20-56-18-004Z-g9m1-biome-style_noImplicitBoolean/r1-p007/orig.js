let toggle = false;
Object.defineProperty(Object.prototype, 'hidden', {
  get() { return toggle = !toggle; }
});
console.log(<div hidden />); // first: true
console.log(<div hidden />); // second: false
console.log(<div hidden={true} />); // explicit
