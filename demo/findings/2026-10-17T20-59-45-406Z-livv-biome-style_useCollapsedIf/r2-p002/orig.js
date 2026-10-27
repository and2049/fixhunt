// Hazard 3: function declaration in block
(function() {
  if (true) {
    if (false) {
      function f() { return 1; }
      return f();
    }
  }
  return typeof f === 'function' ? f() : 0;
})();
