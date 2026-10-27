"use strict";
(() => {
  const re = /\s {2}\s/;
  try {
    eval("re.test('  ')");
    console.log('ok');
  } catch (e) {
    console.log(e.name);
  }
})();
