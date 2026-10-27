function g(a, b = assert.ok(true) || 10, ...rest) {
  console.log(b, rest.length);
}
g(1);
import * as assert from "node:assert/strict";
