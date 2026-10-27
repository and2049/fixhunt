let x = document.createElement('link');
x.href = 'https://fonts.gstatic.com';
console.log(x.getAttribute('rel') ?? 'missing');
x.setAttribute('rel', 'preconnect');
console.log((x.getAttribute('rel') || '') + '-ok');
