let obj = { a: 1 };
let proto = { b: 2 };
obj.__proto__ = proto;
let seen = [];
while (obj.__proto__) {
  seen.push(obj.__proto__.b);
  obj.__proto__ = null;
  break;
}
console.log(seen.length ? seen[0] : 'null');
