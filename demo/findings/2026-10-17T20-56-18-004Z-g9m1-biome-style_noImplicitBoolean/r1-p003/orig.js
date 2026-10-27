const obj = {
  val: 42,
  handler: function() { return this.val; }
};
const extracted = obj.handler;
console.log(<button onClick={extracted.bind(obj)} type="button" />);
console.log(<button onClick={extracted} type="button" disabled />);
