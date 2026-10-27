let count = 0
function inc() { return ++count }

if (!inc() > 0) {
  console.log('first:', count)
} else {
  console.log('second:', count)
}
console.log('final:', count)
