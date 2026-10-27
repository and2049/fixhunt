let counter = 0;
const inc = (function () {
  return ++counter;
});
console.log(inc() + inc());
