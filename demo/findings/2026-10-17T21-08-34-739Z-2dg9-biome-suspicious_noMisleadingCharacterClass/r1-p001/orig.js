const s = 'ÁÁB';
let m; if ((m = s.match(/([Á])+/)) !== null) {
  console.log(m[0]); // ÁÁ
expect_trigger: false,
// After fix: /([A])+/ matches only 'A', not 'Á'
console.log(s.replace(/([A]*)+/, '_')); // _B
