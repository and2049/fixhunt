// Hazard 1: Minimized attribute syntax sensitivity
let html = '';
function render() {
  return `<input${disabled ? ' disabled' : ''} />`;
}
const disabled = true;
html += render();
console.log(html.trim());
