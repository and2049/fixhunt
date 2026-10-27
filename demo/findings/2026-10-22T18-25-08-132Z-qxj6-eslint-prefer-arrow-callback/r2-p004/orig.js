const obj = { prop: null };
let val = obj.prop != null ? obj.prop() : 10;
console.log(val);
val = obj.prop == null ? obj.prop() : 10;
console.log(val);
