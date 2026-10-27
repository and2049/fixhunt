function C() { this.value = 'bound'; }
const BoundC = C.bind({});
try {
  new BoundC();
  console.log('constructed');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
console.log(typeof BoundC.prototype)
