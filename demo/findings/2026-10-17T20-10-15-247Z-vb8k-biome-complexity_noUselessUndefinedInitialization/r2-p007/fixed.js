const obj = {
  val: 42,
  regular: function() {
    var x ;
    return () => {
      console.log(this.val, x);
    };
  }
};
const fn = obj.regular();
fn();
