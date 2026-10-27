const risky = function() {
  throw new Error('intentional');
};
try {
  risky();
} catch (e) {
  console.log(e.name, e.message);
}
