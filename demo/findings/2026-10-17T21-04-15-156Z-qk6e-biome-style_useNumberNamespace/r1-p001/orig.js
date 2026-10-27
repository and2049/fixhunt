"use strict";
const obj = { parseInt: s => s + 'shadow' };
with (obj) {
  console.log(parseInt('1'));
}
