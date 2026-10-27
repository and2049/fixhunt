let count = 0;
const getValue = () => {
  return ++count;
};
let { a: a } = { a: getValue() };
console.log(count);
