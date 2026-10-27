switch (0) {
  case 0:
    function f() { return { y: 1 }; }
    let r = Object.assign({}, f());
    console.log('r.y:', r.y);
    r = ({ ...f() });
    console.log('r.y:', r.y);
    break;
}
