let arr = [1];
let obj = { a: 2 };
try {
  [arr[0]] = [arr[0]] || [3];
  console.log(arr);
} catch (e) {
  console.log('catch pattern:', e.name);
}
try {
  { obj.a } = { obj.a } || { a: 4 };
  console.log(obj);
} catch (e) {
  console.log('catch pattern:', e.name);
}
