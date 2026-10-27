const obj = { toString() { return '='; }, valueOf() { return 0; } };
console.log(/=/.test(obj));
console.log(/=/.test(String(obj)));
