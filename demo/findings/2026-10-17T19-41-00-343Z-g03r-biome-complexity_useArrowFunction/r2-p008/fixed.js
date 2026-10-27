const getValue = (obj) => obj?.prop ?? 'default';
console.log(getValue({ prop: null }));
console.log(getValue({}));
console.log(getValue(undefined));
