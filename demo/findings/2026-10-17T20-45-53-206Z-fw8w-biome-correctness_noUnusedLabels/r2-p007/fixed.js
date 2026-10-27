{
  const obj = { value: 10, getValue: function() { return this.value; } };
  const fn = obj.getValue;
  console.log(obj.getValue(), fn());
}
