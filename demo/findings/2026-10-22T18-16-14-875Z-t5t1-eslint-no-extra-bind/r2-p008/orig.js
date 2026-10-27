let counter = 0;
const inc = (function () {
  return ++counter;
}).bind(null);
console.log(inc() + inc());
