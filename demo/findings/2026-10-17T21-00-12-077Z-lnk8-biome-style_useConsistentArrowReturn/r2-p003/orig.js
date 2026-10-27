(function(){
  'use sloppy mode';
  const obj = { x: 42 };
  let result;
  try {
    // Not triggering rule because with statement makes it not a simple return
    // But we show what happens if someone tried
    result = (() => { with(obj) { return x; } })();
  } catch (e) {
    result = e.name + ': ' + e.message;
  }
  console.log('result:', result);
})();
