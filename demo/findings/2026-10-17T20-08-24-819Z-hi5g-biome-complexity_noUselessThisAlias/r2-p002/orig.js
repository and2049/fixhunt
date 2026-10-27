const obj = { __proto__: { x: 1 }, y: 2 };
const _this = obj;
console.log(_this.__proto__.x + _this.y);
