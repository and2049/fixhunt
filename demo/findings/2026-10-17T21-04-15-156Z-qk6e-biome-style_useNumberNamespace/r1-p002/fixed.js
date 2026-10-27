"use strict";
let Number = { parseInt: s => s + 'reassigned' };
console.log(Number.parseInt('1'));
