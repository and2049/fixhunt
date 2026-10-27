let state = 0;
function getObj() {
  state++;
  return { x: state };
}
let result = {x: state, y: state, ...getObj()};
console.log('state:', state, 'result:', result);
result = ({x: state, y: state, ...getObj()});
console.log('state:', state, 'result:', result);
