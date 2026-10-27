let side = 0;
function inc() { return side++; }
const a = inc();
const b = inc();
const el = <div data-a={a} data-b={b}></div>;
console.log(el.props['data-a'] + el.props['data-b']);
