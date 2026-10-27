const proto = { get undefined() { throw new Error('trapped') } };
Object.setPrototypeOf(globalThis, proto);
try {
  let y = void 0; // removed
  console.log('ok', y);
} catch (e) {
  console.log(e.name, e.message);
}
