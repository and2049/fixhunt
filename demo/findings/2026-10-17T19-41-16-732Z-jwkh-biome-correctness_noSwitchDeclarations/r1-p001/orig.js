function f() {
  let result = [];
  switch (x) {
    case 0:
      try { const y = throw new Error('boom'); } catch (e) { result.push(e.message); }
      break;
    default:
      result.push('ok');
  }
  return result.join('|');
}
let x = 0;
console.log(f());
