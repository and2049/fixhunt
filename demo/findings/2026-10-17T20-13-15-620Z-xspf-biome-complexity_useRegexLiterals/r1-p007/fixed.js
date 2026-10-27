try {
  var re = /\/abc\//;
  console.log(re.test('/abc/'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
