async function main() {
  const gen = (function*() {
    yield 1;
    yield 2;
  })();
  let i = undefined;
  const first = gen.next().value;
  console.log('first yield:', first);
  console.log('i after first yield:', i);
  try { console.log('i after fix:', ({ i, ...{} }).i); } catch(e) { console.log('i after fix error:', e.message); }
}
main();
