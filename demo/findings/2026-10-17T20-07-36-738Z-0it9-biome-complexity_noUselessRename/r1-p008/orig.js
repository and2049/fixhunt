const val = { toString: () => '5', valueOf: () => 10 };
let { p: p } = { p: val };
console.log(+p, `${p}`);
