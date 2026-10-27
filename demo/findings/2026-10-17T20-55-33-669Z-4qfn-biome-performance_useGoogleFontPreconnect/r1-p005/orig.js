const html = '<link href="https://fonts.gstatic.com" />';
console.log(html.includes('<link') && html.includes('fonts.gstatic.com'));
try {
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const link = doc.querySelector('link');
  console.log(link ? 'parsed' : 'failed');
  link.setAttribute('rel', 'preconnect');
  console.log(link.outerHTML);
} catch(e) { console.log(e.name); }
