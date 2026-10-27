let data = {prop: 'outer'}
{
  let data = ({inner: 'value',})
  console.log(data.prop, data.inner)
}
console.log(data.prop)
