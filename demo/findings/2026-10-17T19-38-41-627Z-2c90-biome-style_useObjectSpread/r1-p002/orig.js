let counter = 0;
const src = {
  get value() {
    counter++;
    return counter * 10;
  }
};
const result = Object.assign({}, src);
console.log('result.value:', result.value, 'counter:', counter);
