function html(strings, ...values) {
  return strings.raw[0] + values.map((v, i) => String(values[i]) + strings.raw[i+1]).join('');
}
function test(title, log) {
  log(title);
}
test(html`<b>bold</b>`, msg => console.log('rendered:', msg));
