async function test() {
  const obj = { awaitPromise: Promise.resolve(42) };
  console.log('Start');
  try {
    const val = await Object.hasOwn(obj, 'awaitPromise');
    console.log('Result:', val);
  } catch (e) {
    console.log('Caught:', e.name);
  }
}
test().then(() => console.log('Done'));
