function risky() {
  throw new Error('boom');
}
try {
  const result = !!risky();
  console.log(result);
} catch (e) {
  console.log(e.name, e.message);
}
