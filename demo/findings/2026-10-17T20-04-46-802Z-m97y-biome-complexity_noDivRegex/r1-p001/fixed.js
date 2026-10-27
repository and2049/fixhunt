const obj = { method() { return /[=]/.test(this.value); }, value: 42 };
console.log(obj.method());
const fn = obj.method;
console.log(fn());
