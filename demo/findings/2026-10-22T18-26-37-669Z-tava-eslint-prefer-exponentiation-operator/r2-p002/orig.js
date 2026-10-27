let val = null;
try {
  console.log(Math.pow(val, 2));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
val = undefined;
try {
  console.log(val ** 2);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
