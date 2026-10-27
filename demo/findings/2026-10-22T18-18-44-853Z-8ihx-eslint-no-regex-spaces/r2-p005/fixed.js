let x = /hello {2}world/.test('hello  world')

(() => { console.log('IIFE ran'); })()
console.log(x);
