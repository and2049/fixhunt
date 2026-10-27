CLASS: class C { constructor() { this.x = 1; } }
try {
  new C();
  console.log('ok');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
