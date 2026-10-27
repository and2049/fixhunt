try {
  true && function() { return 1; }();
  console.log('ok');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
