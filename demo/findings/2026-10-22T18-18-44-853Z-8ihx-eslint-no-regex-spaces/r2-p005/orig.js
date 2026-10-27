let x = /hello  world/.test('hello  world')

(() => { console.log('IIFE ran'); })()
console.log(x);
