const obj = {};
Object.defineProperty(obj, 'prop', {
  set(v) { assert.equal(v, 42); }
});
obj.prop = 99;
import * as assert from "node:assert";
