async function* gen() {
  for (const x of Array(Promise.resolve(1)))
    yield await x;
}
gen().next().then(r => console.log('A:', r.value)).catch(e => console.log(e));
async function* g2() {
  for (const x of [...Promise.resolve(1)])
    yield await x;
}
g2().next().then(r => console.log('B:', r.value)).catch(e => console.log(e));
