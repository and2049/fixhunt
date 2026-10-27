console.log(typeof y); // TDZ: should error
let y = `tdz value`;
console.log(y);
