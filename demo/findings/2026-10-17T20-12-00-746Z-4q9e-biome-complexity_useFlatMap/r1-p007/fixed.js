class Base {
  static items = [[1], [2]];
  getData() { return Base.items.flatMap(x => x); }
}
class Der extends Base {
  getData() { return super.getData().length; }
}
console.log(new Der().getData());
