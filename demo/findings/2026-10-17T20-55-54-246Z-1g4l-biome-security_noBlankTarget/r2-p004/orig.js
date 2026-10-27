for (var i = 0; i < 2; i++) { var rel = i === 0 ? 'nofollow' : undefined; const tag = `<a href="/url" target="_blank"${rel ? ` rel=\"${rel}\"` : ''}>${i}</a>`; console.log(tag); }
