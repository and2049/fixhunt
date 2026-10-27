let evalOrder = [];
const push = v => { evalOrder.push(v); return v; };
const expr = (push(1), "ab", push(2), push(3));
console.log('Eval order:', evalOrder.join(','));
console.log('Expr value:', expr);
