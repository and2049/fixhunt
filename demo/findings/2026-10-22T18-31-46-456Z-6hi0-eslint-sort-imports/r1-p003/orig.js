// Hazard 3: __esModule getter order
let log = '';
const originalDefineProperty = Object.defineProperty;
Object.defineProperty = (obj, prop, desc) => {
  if (prop === '__esModule' && desc.get) {
    log += prop;
  }
  return originalDefineProperty.call(obj, prop, desc);
};
import cjs from './commonjs'; // triggers __esModule get
import es from './es6';     // may be moved before it
console.log(log);
