function f() {
  try {
    return assert.ok(true);
  } catch(e) {
    return 'caught';
  }
}
const result = f();
console.log(result);
import * as assert from "node:assert";
