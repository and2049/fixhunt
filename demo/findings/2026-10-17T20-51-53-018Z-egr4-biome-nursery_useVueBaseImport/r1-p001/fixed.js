// Simulate webpack alias: @vue/reactivity -> ./local-reactivity
const originalRequire = require;
function require(id) {
  if (id === '@vue/reactivity') return { ref: () => ({ value: 'patched' }) };
  return originalRequire(id);
}
// --- Rule target ---
import { ref } from 'vue'; // expect_trigger=true
// --------------------
console.log(ref().value);
