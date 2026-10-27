const el = document.createElement('link')
el.href = 'https://fonts.gstatic.com'
(function(){ console.log(el.hasAttribute('rel') ? 'has-rel' : 'no-rel') })()
el.setAttribute('rel', 'preconnect')
console.log(el.getAttribute('rel'));
