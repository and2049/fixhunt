const obj = {
  toString() { return '\\a'; }
};
console.log(String(obj));
