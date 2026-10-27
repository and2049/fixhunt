const obj = { get val() { return side++; }, side: 0 }
let captured;
if (true)
  captured = obj.val
console.log(captured)
