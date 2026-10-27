const obj = {
  base: 2,
  convert(s) { return parseInt(s, this.base) }
}
const fn = obj.convert
console.log(fn.call(obj, '11'))
