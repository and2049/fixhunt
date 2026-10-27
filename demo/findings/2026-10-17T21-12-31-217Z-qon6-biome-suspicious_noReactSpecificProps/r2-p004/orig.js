// Hazard 4: Arguments and rest parameters
function testFn(a, b = getDefault(), ...rest) {
  function getDefault() { return "default"; }
  const attrs = rest.length ? `{...rest}` : "";
  return `<div className=${a || "fallback"} ${attrs}></div>`;
}
console.log(testFn("arg1", undefined, { className: "rest-class" }));
