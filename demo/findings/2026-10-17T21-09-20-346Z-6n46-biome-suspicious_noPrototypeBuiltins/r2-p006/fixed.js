let order = [];
function sideEffect(label) {
  return () => {
    order.push(label);
    return label;
  };
}
const obj = { a: 1 };
order = [];
console.log('Original evaluation order:');
Object.hasOwn(obj, sideEffect('first')());
console.log('Order:', order.join(' -> '));
order = [];
console.log('\nFixed evaluation order:');
Object.hasOwn(obj, sideEffect('first')());
console.log('Order:', order.join(' -> '));
