const obj = { value: 42 };
const getValue = () => `this.value is ${this.value}`;
const bound = getValue.bind(obj);
console.log(bound());
