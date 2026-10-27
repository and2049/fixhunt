let s = null;
try {
  console.log(s.trimLeft());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
