let callCount = 0;
function getObj() {
  callCount++;
  return { x: callCount };
}
let result = Object.assign(getObj(), { y: 2 });
console.log(callCount, result.x, result.y); // 1, 1, 2
result = ({ ...getObj(), y: 2 });
console.log(callCount, result.x, result.y); // 2, 2, 2 (called twice)
