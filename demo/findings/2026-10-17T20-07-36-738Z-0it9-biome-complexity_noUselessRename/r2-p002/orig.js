function f() {
  let {arguments: arguments} = arguments;
  return function g() {
    console.log('args length:', arguments.length);
    return arguments[0];
  };
}
const g = f();
g(10, 20);
g(99);
