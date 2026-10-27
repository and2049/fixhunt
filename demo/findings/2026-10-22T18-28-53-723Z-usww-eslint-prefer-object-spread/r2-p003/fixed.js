function outer() {
  const x = { a: 1 };
  if (true) {
    let x = { b: 2 }; // shadows outer x
    console.log(({ ...x}).a); // undefined, x is inner
    console.log(({ ...x }).a);           // undefined
  }
}
outer();
