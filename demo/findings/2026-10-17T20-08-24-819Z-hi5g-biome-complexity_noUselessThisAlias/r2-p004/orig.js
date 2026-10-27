for (let i = 0; i < 2; i++) {
  var self = i;
  (() => console.log(self))();
}
