// Internal Vue reactivity returns objects with custom valueOf used in reactive calculations
let reactiveValue;
// --- Rule target ---
import { reactive } from 'vue'; // expect_trigger=true
// --------------------
reactiveValue = reactive({ value: 5 });
// Object with custom valueOf that returns a BigInt
const obj = { valueOf: () => 3n };
console.log(String(reactiveValue.value + obj)); // Should be '8' if reactive unwraps correctly
console.log(`${reactiveValue.value}${obj}`);   // Template literal: relies on String() coercion
