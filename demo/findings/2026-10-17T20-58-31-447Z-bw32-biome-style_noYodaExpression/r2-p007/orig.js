async function seq() {
  let a = await Promise.resolve(1);
  if (\"1\" == a) console.log('equal'); // rule triggers
  return a;
}
seq().then(r => console.log('result:', r));
