switch(1) {
  case 1:
    var f = undefined;
    console.log(f === undefined ? 'yes' : 'no');
    function f() { return 1; }
    console.log(typeof f);
    break;
}
