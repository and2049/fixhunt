const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return assert.ok(true) && 42; },
  set(v) { assert.equal(v, 42); }
});
console.log(obj.prop);
obj.prop = 99;
import * as assert from "node:assert/strict";
