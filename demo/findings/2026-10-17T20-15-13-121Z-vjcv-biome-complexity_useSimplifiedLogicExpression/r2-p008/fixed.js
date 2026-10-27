const obj = {
  [Symbol.toPrimitive](hint) {
    return hint === 'string' ? 'str' : 42;
  }
};
let res = String(obj);
console.log(res);
