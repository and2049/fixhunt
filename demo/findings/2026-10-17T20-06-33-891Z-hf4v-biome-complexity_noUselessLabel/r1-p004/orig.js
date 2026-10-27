async function* gen() {
  lbl: while (true) {
    const v = await Promise.resolve(1);
    console.log('yield:', v);
    if (v === 1) break lbl;
  }
}
(async () => {
  for await (const x of gen()) {
    console.log('got:', x);
    break;
  }
})();
