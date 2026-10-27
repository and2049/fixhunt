let f = function () {
  console.log(this === undefined ? 'strict' : this);
}.bind(null) /* preserve this comment */;
f();
