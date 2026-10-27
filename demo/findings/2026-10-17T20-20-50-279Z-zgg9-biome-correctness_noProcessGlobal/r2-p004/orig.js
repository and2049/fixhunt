const x = process // keep this value
console.log(x === globalThis.process ? 'same' : 'diff');
