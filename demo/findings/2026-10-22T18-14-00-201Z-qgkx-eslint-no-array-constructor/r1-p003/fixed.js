const obj = [];
obj.__proto__ = { x: 1 };
console.log(obj.hasOwnProperty('__proto__'));
try { 
  const arr = [...[]]; // dummy trigger
  arr.__proto__ = { y: 2 };
  console.log(arr.hasOwnProperty('__proto__')); 
} catch(e) {}
