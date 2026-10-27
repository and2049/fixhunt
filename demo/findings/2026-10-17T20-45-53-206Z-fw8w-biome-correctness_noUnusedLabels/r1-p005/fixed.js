{
  const obj = {
    val: 42,
    fn: function() { return this.val; },
    arr: () => this.val
  };
  console.log(obj.fn(), obj.arr());
  const f = obj.fn;
  const a = obj.arr;
  console.log(f.call(obj), a.call(obj));
}
