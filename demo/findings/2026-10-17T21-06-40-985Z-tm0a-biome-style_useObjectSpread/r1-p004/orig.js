function f() {
  for (var i = 0; i < 2; i++) {
    var tmp = Object.assign({}, {val: i})
    console.log(tmp.val)
  }
  console.log(typeof tmp)
}
f()
