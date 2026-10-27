(function() {
  var trimLeft = function() { return 'BAD'; };
  with ({ s: '   x   ' }) {
    console.log(s.trimLeft());
  }
})();
