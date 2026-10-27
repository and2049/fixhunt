const x = { toString: () => 42 };
console.log('+ coercion:', __dirname + x);
console.log('template:', `${__dirname}${x}`);
console.log('import.meta + x:', import.meta.dirname + x);
