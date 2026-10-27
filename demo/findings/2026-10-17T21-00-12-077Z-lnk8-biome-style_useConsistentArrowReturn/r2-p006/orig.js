let defined = false;
let value = 99;
const target = {};

// Define a setter with side effect
Object.defineProperty(target, 'prop', {
  set(v) {
    defined = true;
    value = v * 2;
  }
});

// Arrow returning object literal - rule triggers
const makeObj = (v) => { return { prop: v }; };

makeObj(5);
console.log('defined:', defined);
console.log('value:', value);
