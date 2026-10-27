"use strict";
async function f() {
  let x = 0;
  const inc = () => ++x;
  const v = await Promise.resolve(parseInt(String(inc())));
  return v + x;
}
f().then(console.log);
