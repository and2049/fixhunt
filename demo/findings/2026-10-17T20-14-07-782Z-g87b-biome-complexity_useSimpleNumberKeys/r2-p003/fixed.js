
let x = 1;
(function() {
  const obj = { 1000: x }; // rewritten to 1000
  let x = 2; // shadows outer x
  console.log(obj[1000] === 1 ? 'outer' : 'inner');
})();
