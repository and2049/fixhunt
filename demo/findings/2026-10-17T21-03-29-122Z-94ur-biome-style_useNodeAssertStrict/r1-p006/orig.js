class C {
  static x = assert.ok(true) && 1;
  y = assert.equal(1, 1) && 2;
}
console.log(C.x, new C().y);
import * as assert from "node:assert";
