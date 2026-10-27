const props = { children: 'unexpected', className: 'box' };
let result = '';
const el = <div {...props}></div>;
if (el.props && el.props.children) {
  result += el.props.children;
}
console.log(result);
