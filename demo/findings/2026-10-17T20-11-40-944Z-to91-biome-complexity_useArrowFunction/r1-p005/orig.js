{ let x = 1;
  if (true) {
    function f() { return x; }
    console.log(f());
    let f = function() { return x + 1; };
    console.log(f());
  }
}
