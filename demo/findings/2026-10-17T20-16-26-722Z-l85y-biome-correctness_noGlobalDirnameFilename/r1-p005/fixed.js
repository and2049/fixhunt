// Hazard 5
const maybePath = null;
const result = maybePath?.startsWith(import.meta.dirname) ?? 'fallback';
console.log(result);
