let y = undefined;
if (!x) {
  throw new Error('TDZ');
}
x = 1;
y = 2;
console.log(x);
import { x } from './m1.js';
