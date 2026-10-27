const obj = { __proto__: { toString: () => 'proto' }, toString: () => 'obj' };
lbl: {
  console.log(obj.toString());
  break lbl;
}
console.log(Object.assign({}, obj).toString());
