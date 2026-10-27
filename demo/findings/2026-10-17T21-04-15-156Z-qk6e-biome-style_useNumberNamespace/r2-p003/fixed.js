let Number = 42;
try {
  console.log(typeof Number.parseInt('1'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
