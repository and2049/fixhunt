'use strict';
try {
  let c = (d = 1);
} catch(e) {
  console.log(e.name, e.message);
}
