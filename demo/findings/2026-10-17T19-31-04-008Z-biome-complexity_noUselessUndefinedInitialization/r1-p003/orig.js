async function main() {
  let x;
  const p = Promise.resolve().then(() => console.log(typeof x));
  x = 42;
  await p;
}
main();
