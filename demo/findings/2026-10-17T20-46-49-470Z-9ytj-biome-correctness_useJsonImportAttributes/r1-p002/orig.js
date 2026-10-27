const getData = () => {
  import obj from './data.json';
  return () => obj.prop; // captures obj via closure
};
const fn = getData();
console.log(fn());
