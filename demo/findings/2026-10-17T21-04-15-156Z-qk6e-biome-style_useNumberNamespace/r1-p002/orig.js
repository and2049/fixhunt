"use strict";
let Number = { parseInt: s => s + 'reassigned' };
console.log(parseInt('1'));
