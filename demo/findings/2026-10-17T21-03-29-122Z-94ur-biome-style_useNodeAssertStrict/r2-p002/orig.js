const mod = 'node:' + 'assert';
const assert = require(mod);
try {
  assert.ok(0, 0);
} catch (e) {
  console.log(e.name, e.message);
}
