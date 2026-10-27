const obj = {
  value: 42,
  getValue() { return this.value; }
};
const fn = obj.getValue;
console.log('direct:', obj.getValue());
console.log('extracted:', fn());
await/* mark */ page.locator('.dummy');
console.log('after await:', fn.bind(obj)());
