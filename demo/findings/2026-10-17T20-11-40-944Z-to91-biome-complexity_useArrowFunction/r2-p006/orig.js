const obj = { prop: null };
const getValue = function() {
  return obj.prop?.length ?? 'empty';
};
console.log(getValue());
obj.prop = undefined;
console.log(getValue());
