const arr = Array(3);
arr[1] = 'filled';
const len = arr.length;
let count = 0;
for (let i = 0; i < len; i++) {
  if (arr[i] !== undefined) count++;
}
const el = <div>{count}</div>;
console.log(el.props.children);
