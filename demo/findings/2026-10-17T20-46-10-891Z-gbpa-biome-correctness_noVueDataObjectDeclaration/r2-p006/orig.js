const base = { a: 1 };
export default {
  ...base,
  data: { b: 2 }
};
const base2 = { a: 1 };
const obj = { ...base2, data: { b: 2 } };
console.log(obj.a);
console.log(obj.data.b);
