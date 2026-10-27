let value = null;
console.log(value?.match(/a  b/));
value = undefined;
console.log(value?.match(/a  b/) ?? 'nullish');
