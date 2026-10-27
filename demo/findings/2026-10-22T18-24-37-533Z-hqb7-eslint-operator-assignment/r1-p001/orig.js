async function* g() {
  let i = 0;
  while (i < 3) {
    const v = await Promise.resolve(i);
    if ((yield i++) === undefined) continue;
    i = i + v; // TRIGGER
    console.log('state:', i);
  }
}
(async () => {
  const iter = g();
  for await (const x of iter) console.log('yielded:', x);
})().catch(e => console.error(e));
