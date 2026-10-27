const obj = {};
if ('a' in obj) {
  obj.a = 1;
} else if ('__proto__' in obj) {
    obj.__proto__ = {toString:()=>'proto'};
    console.log(obj.toString());
  }
console.log('__proto__ present:', '__proto__' in obj);
