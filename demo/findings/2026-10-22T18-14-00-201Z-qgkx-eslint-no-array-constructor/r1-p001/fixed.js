function f() {
  'use strict';
  const { length } = arguments;
  let args = [];
  for (let i = 0; i < length; i++) args[i] = arguments[i];
  try { return Array(...args); }
  catch (e) { return e instanceof TypeError ? 'TypeError:' + e.message : 'other'; }
}
console.log(f(1, 2));
