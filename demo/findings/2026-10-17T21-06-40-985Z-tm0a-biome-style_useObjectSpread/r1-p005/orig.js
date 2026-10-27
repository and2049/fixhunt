let data = {prop: 'outer'}
{
  let data = Object.assign({}, {inner: 'value'})
  console.log(data.prop, data.inner)
}
console.log(data.prop)
