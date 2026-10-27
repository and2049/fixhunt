const obj = { value: 42, get flag() { return this.value > 0; } };
const extract = obj.flag;
console.log('Before:', !!extract.call({value: -1}));
console.log('After fix:', extract.call({value: -1})); // Rule would rewrite !!extract to extract
console.log('Original obj:', !!obj.flag);
console.log('Fixed obj:', obj.flag);
