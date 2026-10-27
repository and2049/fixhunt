const x = { toString: () => 42 };
console.log('+ coercion:', import.meta.dirname + x);
console.log('template:', `${import.meta.dirname}${x}`);
console.log('import.meta + x:', import.meta.dirname + x);
