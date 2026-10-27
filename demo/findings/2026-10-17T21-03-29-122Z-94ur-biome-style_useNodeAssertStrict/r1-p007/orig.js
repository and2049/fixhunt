import * as assert from "node:assert";
console.assert(typeof assert.equal === 'function');
try {
  assert.equal(1, 1);
  console.log('equal worked');
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
