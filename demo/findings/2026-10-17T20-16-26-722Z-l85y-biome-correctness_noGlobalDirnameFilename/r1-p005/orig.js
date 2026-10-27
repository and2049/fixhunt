// Hazard 5
const maybePath = null;
const result = maybePath?.startsWith(__dirname) ?? 'fallback';
console.log(result);
