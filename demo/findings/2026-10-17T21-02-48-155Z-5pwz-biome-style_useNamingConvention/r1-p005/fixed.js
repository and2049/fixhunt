function f(FirstParam) {
  return FirstParam * 2;
}
let Constructor = window[f.name];
let instance = new Constructor(5);
console.log(instance instanceof f ? 'ok' : 'fail', instance.constructor === f ? 'same' : 'diff');
