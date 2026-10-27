let x = undefined;
(function f() {
  console.log(x == null);
  let y = x?.prop ?? 'ok';
  console.log(y);
})();
