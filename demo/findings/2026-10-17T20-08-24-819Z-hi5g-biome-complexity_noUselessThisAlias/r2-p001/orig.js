const self = 42;
function outer() {
  const self = this;
  return () => {
    console.log(self);
  };
}
outer()(100);
