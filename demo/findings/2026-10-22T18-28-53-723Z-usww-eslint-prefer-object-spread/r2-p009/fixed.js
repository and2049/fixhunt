function outer() {
  const x = { a: 1 };
  if (true) {
    let x = { b: 2 };
    console.log('outer.x.a:', ({ ...x}).a);
    console.log('outer.x.a:', ({ ...x }).a);
  }
}
outer();
