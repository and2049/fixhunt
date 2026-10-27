async function test() {
  let ok = false;
  if (ok) {
    await Promise.resolve(1);
  } else if (!ok) {
      const res = await Promise.resolve(2);
      console.log('got', res);
    }
  console.log('end');
}
test().catch(e => console.error(e));
