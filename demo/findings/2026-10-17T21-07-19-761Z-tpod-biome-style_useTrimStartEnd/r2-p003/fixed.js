async function test() {
  const p = Promise.resolve('  world');
  const a = await p;
  const b = a.trimEnd();
  console.log(`'${b}'`);
}
test().catch(e => console.error(e));
