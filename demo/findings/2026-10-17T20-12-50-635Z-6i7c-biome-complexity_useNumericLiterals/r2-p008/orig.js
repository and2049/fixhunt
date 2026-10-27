let callCount = 0
const obj = {
  get value() {
    callCount++
    return '101'
  }
}
console.log(parseInt(obj.value, 2), callCount)
console.log(parseInt(obj.value, 2), callCount)
