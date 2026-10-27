let obj = null;
console.log(obj?.m?.());
obj = { m() { return 'hit'; } };
console.log(obj?.m?.());
obj = { m: undefined };
console.log(obj?.m?.());
