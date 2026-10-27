let r = '';
const obj = { toString: () => { r += 'x'; return 42; } };
console.log(('start' + (obj, obj)) === ('start' + `${obj}${obj}`));
