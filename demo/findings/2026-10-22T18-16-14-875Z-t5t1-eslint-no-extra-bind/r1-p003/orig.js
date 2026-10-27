const obj = {
  m: function () {
    return this.value;
  }.bind({value: 42})
};
console.log(obj.m());
console.log(obj.m.call({value: 99}));
