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
obj.hasOwnProperty(sideEffect('first')());
console.log('Order:', order.join(' -> '));
order = [];
console.log('\nFixed evaluation order:');
Object.prototype.hasOwnProperty.call(obj, sideEffect('first')());
console.log('Order:', order.join(' -> '));
