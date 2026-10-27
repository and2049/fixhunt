// Hazard 7: Global side-effect dependency
window.globalState = 0;
import { triggerSideEffect } from './mod1'; // sets globalState = 42
import { useSideEffect } from './mod2';   // reads globalState
console.log(useSideEffect()); // should be 42, but if swapped, triggerSideEffect not run yet
