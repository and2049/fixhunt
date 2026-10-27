async function seq() {
  const x = await Promise.resolve(1);
  console.log(x); // 1
  const y = `unused`; // triggers rule
  console.log(y); // 'unused'
  return y;
}
seq().then(r => console.log('result:', r));
