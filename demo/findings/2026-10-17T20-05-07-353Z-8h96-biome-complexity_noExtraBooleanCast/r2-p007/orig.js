const obj = { prop: null };
console.log(!!obj?.prop);
if (!!obj?.prop) {
  console.log('truthy');
} else {
  console.log('falsy or nullish');
}
