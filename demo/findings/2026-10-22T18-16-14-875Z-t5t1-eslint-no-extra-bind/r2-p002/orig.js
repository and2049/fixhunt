"use strict";
const f = (function () { return typeof this; }).bind(null);
const g = f;
console.log(g());
