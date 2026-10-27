const relProp = 'nofollow'; const html = `<a href="/url" target="_blank" ${relProp ? `rel=\"${relProp}\"` : ''}>text</a>`; console.log(html);
