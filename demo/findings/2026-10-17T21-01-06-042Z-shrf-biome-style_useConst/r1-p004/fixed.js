'use strict';
try {
  const c = (d = 1);
} catch(e) {
  console.log(e.name, e.message);
}
