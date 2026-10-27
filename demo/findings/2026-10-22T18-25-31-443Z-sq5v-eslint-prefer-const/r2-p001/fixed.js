function f(a = g(), ...rest) {
  const len = arguments.length;
  console.log('len:', len, 'a:', a, 'rest:', rest.join(',')||'empty');
}
function g() { return 1; }
f();
