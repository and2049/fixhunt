// Internal Vue reactivity only exposes ref, reactive
// Main vue also exposes defineComponent (which we don't want here)
let VueReactivity;
// --- Rule target ---
import * as VueReactivity from '@vue/reactivity'; // expect_trigger=true
// --------------------
if ('defineComponent' in VueReactivity) {
  console.log('ERROR: defineComponent leaked into reactivity namespace');
} else {
  console.log('OK: only reactivity exports present');
}
