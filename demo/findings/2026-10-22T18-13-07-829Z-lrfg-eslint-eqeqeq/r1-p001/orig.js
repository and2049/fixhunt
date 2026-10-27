const obj = { valueOf: () => { console.log('valueOf called'); return 0; } };
console.log(obj == 0);
console.log(obj === 0);
