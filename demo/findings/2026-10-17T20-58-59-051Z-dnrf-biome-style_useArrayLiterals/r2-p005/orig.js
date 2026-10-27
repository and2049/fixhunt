"use strict";
let result;
try {
  result = eval("Array(1, 2)");
} catch (e) {
  result = e;
}
console.log(result instanceof Array && result.length === 2);
