// Hazard 4: Side effects in import specifiers
let log = [];
function sideEffect(x) { log.push(x); return x; }
import { [sideEffect('a')]: foo } from './obj'; // may be moved
import { bar } from './obj';                    // may be moved
console.log(log.join(','));
