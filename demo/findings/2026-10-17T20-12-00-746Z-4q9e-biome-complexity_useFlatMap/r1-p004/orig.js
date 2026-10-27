const src = [[1], [2]];
const mapped = src.map(x => x);
const flattened = mapped.flat();
console.log(mapped === src, mapped === flattened);
// After fix, no intermediate array -> mapped would be undefined
