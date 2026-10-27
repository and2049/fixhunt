let obj = { __proto__: { value: 1 } };
if (!!obj.__proto__) { // triggers rule: !! on object
  console.log(obj.value); // reads from prototype
}
obj.__proto__ = null;
console.log(!obj.__proto__); // now falsy
