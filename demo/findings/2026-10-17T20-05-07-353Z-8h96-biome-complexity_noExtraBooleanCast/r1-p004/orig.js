const arr = Array(3);
arr[1] = 'present';
console.log('Length:', arr.length);
console.log('Holes via !!length:', !!arr.length ? 'truthy' : 'falsy');
let i = 0;
while (!!arr.length && i < 5) {
  console.log('Index:', i, 'Value:', arr[i]);
  i++;
}
// Fix would make condition `arr.length` — same numeric value, but highlights reliance on explicit bool
