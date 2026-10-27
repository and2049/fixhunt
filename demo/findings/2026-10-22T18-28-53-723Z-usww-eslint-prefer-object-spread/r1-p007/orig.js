let obj = null;
try {
  Object.assign({}, obj);
} catch (e) {
  console.log(e.name);
}
obj = undefined;
try {
  Object.assign({}, obj);
} catch (e) {
  console.log(e.name);
}
