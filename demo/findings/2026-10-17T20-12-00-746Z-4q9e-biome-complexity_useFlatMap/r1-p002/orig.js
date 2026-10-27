const arr = [1, , 3];
const mapped = arr.map((x, i) => i === 1 ? undefined : [x]);
const flattened = mapped.flat();
console.log(flattened.length, flattened.join(','));
try {
  const flatMapped = arr.flatMap((x, i) => i === 1 ? undefined : [x]);
  console.log(flatMapped.length, flatMapped.join(','));
} catch (e) { console.log(e.name + ': ' + e.message); }
