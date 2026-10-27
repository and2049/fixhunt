let count = 0;
const obj = {
  get prop() {
    count++;
    return 42;
  }
};
console.log(obj.prop == 42);
console.log(count);
