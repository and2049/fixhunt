async function* gen() { yield 1; yield* [2, 3]; }
(async () => {
  const arr = [];
  for await (const x of gen()) arr.push(x);
  console.log('collected:', arr);
  const mapped = arr.map(x => [x, x * 2]);
  console.log('mapped:', mapped);
  const result = mapped.flat();
  console.log('flat:', result);
})();
