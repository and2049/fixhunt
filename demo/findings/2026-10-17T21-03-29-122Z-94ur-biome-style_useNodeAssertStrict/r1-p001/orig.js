import * as assert from "node:assert";
let x = 0;
try {
  assert.ok(x == 0);
  console.log('non-strict ok');
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
try {
  assert.deepEqual([], []);
  console.log('deepEqual ok');
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
