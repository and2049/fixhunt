console.log(typeof process); // should be 'object' before fix
let process = { version: 'local' };
console.log(process.version);
