let x = 1
(function () {
  console.log('called');
}).bind(null)
[x] = [x + 1]
console.log(x)
