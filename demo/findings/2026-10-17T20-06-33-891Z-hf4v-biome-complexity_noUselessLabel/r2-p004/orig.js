let obj = { prop: { value: 5 } };
let result;
label: if ((obj?.prop ?? {value: 0}).value > 0) {
  result = obj.prop.value;
  break label;
} else {
  result = -1;
}
console.log(result);
