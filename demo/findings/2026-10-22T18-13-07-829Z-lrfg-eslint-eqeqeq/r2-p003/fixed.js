'use strict'
function f() { return this }
console.log((f() == undefined) ? 'undef' : 'defined')
console.log((f() === undefined) ? 'undef' : 'defined')
