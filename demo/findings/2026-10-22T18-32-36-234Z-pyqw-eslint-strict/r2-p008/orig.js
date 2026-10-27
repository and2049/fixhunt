const obj = {
  toString() { return 'hello';
  },
  valueOf() { return 42;
  }
};
console.log(String(obj));
console.log(obj + '');
console.log(`${obj}`);
