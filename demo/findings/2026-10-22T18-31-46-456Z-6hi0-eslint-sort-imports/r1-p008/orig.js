// Hazard 8: Sparse array and array-like confusion
import { createArrayLike } from './arraylike'; // returns {0: 'a', length: 1}
import { Array } from './array-shim';         // may override global Array
const arr = createArrayLike();
console.log(Array.isArray(arr)); // false if shimmed, true otherwise — depends on import order
