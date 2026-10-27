async function* ag() {
  yield await Promise.resolve(1);
  return;
}
(async () => {
  const it = ag();
  const r1 = await it.next();
  console.log(r1.value, r1.done); // 1 false
  const r2 = await it.next();
  console.log(r2.value, r2.done); // undefined true
})();
// No return; at end to remove — testing near-miss: yield after await
}
