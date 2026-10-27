let x = null;
console.log('x?.prop?.Math?.pow?.(2,3):', x?.prop?.Math?.pow?.(2, 3));

x = { prop: { Math: { pow: (b, e) => b ** e } } };
console.log('x?.prop?.Math?.pow?.(2,3):', x?.prop?.Math?.pow?.(2, 3));

// Direct call that rule would fire on
const base = 2;
exp = 3;
console.log('Math.pow(base,exp):', base**exp);
console.log('base ** exp:', base ** exp);
