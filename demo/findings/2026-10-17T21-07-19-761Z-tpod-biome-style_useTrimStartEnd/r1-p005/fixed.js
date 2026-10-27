let s = null;
try {
  console.log(s.trimStart());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
