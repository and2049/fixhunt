async function f() {
  let x = 0;
  for (let i = 0; i < 2; i++) {
    await Promise.resolve().then(() => ++x);
  }
  return x;
}
f().then(console.log).catch(e=>console.error(e));
