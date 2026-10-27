function f() {
  console.log(this === global);
}
const o = {m: f};
(o.m || o.n)(); // calls f with this=global due to [[Get]] returning undefined
