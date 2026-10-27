async function f() {
  let x = 0;
  for (let i = 0; i < 2; i++) {
    await Promise.resolve().then(() => ++x);
    continue; // <-- removes this, moves await earlier logically? Actually same order.
  }
  return x;
}
f().then(console.log).catch(e=>console.error(e));
