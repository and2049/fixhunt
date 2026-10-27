const obj = { value: 1, getValue() { return this.value; } };
let f = obj.getValue;
let result = (f ||= obj.getValue.bind(obj));
console.log('bound result:', result());
f = obj.getValue;
f &&= obj.getValue.bind(obj);
console.log('bound result2:', f());
