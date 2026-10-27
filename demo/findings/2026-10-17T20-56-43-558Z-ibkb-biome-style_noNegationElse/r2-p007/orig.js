let x = 1, y = 2
if (!x + y > 2) {
  console.log('less')
} else {
  console.log('greater or equal')
}
x = 3
console.log(!x + y > 2 ? 'static' : 'dynamic')
