let value = null;
const obj = {value};
// After fix: {value}
console.log(obj.value ?? 'nullish');
console.log((obj.value ?? 'nullish') === 'nullish');
value = undefined;
console.log(obj.value ?? 'nullish');
console.log((obj.value ?? 'nullish') === 'nullish');
