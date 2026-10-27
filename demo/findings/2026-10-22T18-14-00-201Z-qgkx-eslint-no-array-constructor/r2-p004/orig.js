const a = undefined;
const b = a?.length ?? Array(1, 2)[0];
console.log(b);
