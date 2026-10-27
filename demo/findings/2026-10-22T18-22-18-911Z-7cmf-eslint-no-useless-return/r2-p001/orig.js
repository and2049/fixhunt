function outer() {
  inner:
    {
      function innerFunc() { return; }
      break inner;
    }
  console.log('A');
}
outer();
