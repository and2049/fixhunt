function makeLink(...args) {
  const lnk = document.createElement('link');
  lnk.href = args[0] || 'https://fonts.gstatic.com';
  arguments[0] = 'changed';
  return lnk;
}
const l1 = makeLink();
console.log(l1.getAttribute('rel'));
l1.setAttribute('rel', 'preconnect');
console.log(l1.getAttribute('rel'));
const l2 = makeLink();
console.log(l2.getAttribute('href'));
