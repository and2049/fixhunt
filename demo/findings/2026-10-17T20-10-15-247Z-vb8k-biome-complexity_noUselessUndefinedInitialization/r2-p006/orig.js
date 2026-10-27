let y;
try {
  y = undefined;
  throw new Error('test');
} catch (e) {
  console.log(y === undefined, e.message);
}
