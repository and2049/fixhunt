let ssrHtml = '<a href="/url" target="_blank" data-ext="track">link</a>';
console.log('SSR HTML:', ssrHtml.includes('rel') ? 'has rel' : 'no rel');
