let val = -0;
console.log('String(!!val):', String(!!val));
console.log('String(val):', String(val));
val = 0;
console.log('String(!!val):', String(!!val));
console.log('String(val):', String(val));
// Rule would fix !!val to val in String() context — showing divergent outputs
