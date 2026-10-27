function html(strings) {
  return strings.raw.join('');
}
const result = html`<div>content</div>`;
console.log(result); // <div>content</div>
// Rule silent because tagged -> considered used
