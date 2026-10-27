try {
  true && function() { return 1; }();
} catch (e) {
}
