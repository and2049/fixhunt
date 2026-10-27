function outer() {
  inner:
    {
      function innerFunc() {  }
      break inner;
    }
  console.log('A');
}
outer();
