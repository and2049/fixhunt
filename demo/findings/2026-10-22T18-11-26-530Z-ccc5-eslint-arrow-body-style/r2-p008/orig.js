let counter = 0;
const inc = () => counter++;
const val = (inc(), inc());
console.log(counter, val);
