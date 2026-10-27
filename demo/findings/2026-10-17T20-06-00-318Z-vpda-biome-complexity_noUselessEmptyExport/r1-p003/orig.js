var scoped = 'module-only';
export {};
function check() {
  return typeof scoped !== 'undefined' && !globalThis.hasOwnProperty('scoped');
}
console.log(check());
