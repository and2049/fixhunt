switch (1) {
  case 1:
    function f({ p }) { return p; }
    break;
}
console.log(f({ p: 88 })); // Should print 88 if fix preserves function
