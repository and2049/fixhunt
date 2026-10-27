const self = 42;
function outer() {
  return () => {
    console.log(this);
  };
}
outer()(100);
