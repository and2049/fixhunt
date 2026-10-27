const href = { toString: () => 'https://fonts.gstatic.com' };
const link = document.createElement('link');
link.href = href;
console.log(link.outerHTML)
