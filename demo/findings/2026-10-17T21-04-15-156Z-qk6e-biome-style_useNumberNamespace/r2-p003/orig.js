let Number = 42;
try {
  console.log(typeof parseInt('1'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
