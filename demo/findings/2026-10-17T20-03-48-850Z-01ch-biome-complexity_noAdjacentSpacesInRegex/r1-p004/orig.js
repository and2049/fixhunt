"use strict";
(() => {
  const re = /\s  \s/;
  try {
    eval("re.test('  ')");
    console.log('ok');
  } catch (e) {
    console.log(e.name);
  }
})();
