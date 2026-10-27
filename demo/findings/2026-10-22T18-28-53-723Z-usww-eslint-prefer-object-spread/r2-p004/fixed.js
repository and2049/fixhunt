switch (0) {
  case 0:
    function f() { return { y: 1 }; }
    let r = { ...f()};
    console.log(r.y); // 1
    r = ({ ...f() });
    console.log(r.y); // 1
    break;
}
