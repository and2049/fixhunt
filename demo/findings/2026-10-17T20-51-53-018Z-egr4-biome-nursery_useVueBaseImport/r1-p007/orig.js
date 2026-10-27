// Simulate TS type-only import behavior at runtime via structural check
let RefType;
// --- Rule target ---
import type { Ref } from '@vue/reactivity'; // expect_trigger=true (simulated)
// --------------------
// In real TS, this would be erased; here we simulate by checking if Ref is a type-like object
// We assume @vue/reactivity exports Ref as a type, but main 'vue' does not in this scenario
if (typeof Ref === 'undefined') {
  console.log('Ref type not available in main vue - simulation of TS error');
} else {
  console.log('Ref type available');
}
