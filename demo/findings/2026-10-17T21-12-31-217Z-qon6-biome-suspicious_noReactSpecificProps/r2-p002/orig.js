// Hazard 2: Function declarations inside blocks
if (true) {
  function getClassName() { return "block-fn"; }
  const div = `<div className=${getClassName()}></div>`;
  console.log(div);
}
// After fix: className -> class, but function scope remains
try { console.log(typeof getClassName); } catch(e) { console.log(e.name); }
