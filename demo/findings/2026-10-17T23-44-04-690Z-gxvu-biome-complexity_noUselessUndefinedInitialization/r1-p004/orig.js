"use strict";
(() => {
  console.log(typeof z); // Error if z not declared yet
  let z = undefined; // Rule triggers
  console.log(z);
})();
