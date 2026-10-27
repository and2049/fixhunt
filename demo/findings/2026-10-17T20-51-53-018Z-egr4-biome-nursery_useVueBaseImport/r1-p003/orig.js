// Simulate conditional exports: 'vue' -> esm, '@vue/*' -> cjs
const modules = {
  vue: { ref: () => ({ value: 'esm-ref' }) },
  '@vue/reactivity': { ref: () => ({ value: 'cjs-ref' }) }
};
function require(id) { return modules[id]; }
// --- Rule target ---
import { ref } from '@vue/reactivity'; // expect_trigger=true
// --------------------
console.log(ref().value);
