function test(a, b = () => <div className={a}></div>, ...rest) {
  console.log(arguments.length, rest.length);
  return b();
}
test(1);
