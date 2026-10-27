let value = null;
console.log(value?.match(/a {2}b/));
value = undefined;
console.log(value?.match(/a {2}b/) ?? 'nullish');
