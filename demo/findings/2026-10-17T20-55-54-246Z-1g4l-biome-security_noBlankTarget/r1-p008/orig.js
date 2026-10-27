const linker = {
  html: '<a href="/url" target="_blank">link</a>',
  getHtml: function() { return this.html; }
};
const fn = linker.getHtml;
console.log('Extracted fn:', fn());
