function foo(a, b = 1, ...rest) {
  return () => {
    console.log(arguments.length, rest.length);
    return <div disabled arguments={arguments.length} />;
  };
}
const fn = foo(1, 2, 3);
fn();
