let y = 5;
let { z: /* preserve this */ z } = { z: y };
console.log(z);
