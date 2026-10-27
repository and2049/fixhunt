let arr = [, , 3];
let sum = 0;
while (arr.length > 0) {
  const v = arr.pop();
  if (v !== undefined) sum += v;
}
console.log(sum);
