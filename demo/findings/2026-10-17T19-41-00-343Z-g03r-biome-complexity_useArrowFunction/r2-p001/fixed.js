function outer() {
  let f = 1;
  const x = () => {
    console.log('inner:', f);
    return f++;
  };
  for (let i = 0; i < 2; i++) {
    const f = 10;
    console.log(x());
  }
}
outer();
