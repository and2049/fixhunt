let RegExp = String;
try {
  var re = new RegExp('a', '');
  console.log(re);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
