const g = Function('return this')();
defineProperty(g, 'Number', { value: undefined });
try {
  console.log(parseInt('1'));
} catch (e) {
}
function defineProperty(obj, name, desc) { Object.defineProperty(obj, name, desc); }
