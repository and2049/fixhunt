let pattern = /\u0068\u0072\u0065\u0066/g;
pattern.lastIndex = 0;
const html = '<a href="/url" target="_blank">click</a>';
console.log('match:', pattern.exec(html));
