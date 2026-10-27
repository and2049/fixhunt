let x = null;
console.log(x?.toFixed() ?? 'nullish');
x = 0;
console.log(x?.toFixed() ?? 'falsy zero');
x = undefined;
console.log(x?.toFixed() ?? 'undefined');
x = false;
console.log(x?.toFixed() ?? 'falsy false');
