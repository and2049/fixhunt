let result
(() => {
  const r = ({x: 1,})
  return r.x
})().then(v => {
  console.log('result:', v)
}).catch(e => {
  console.error('error:', e.message)
});
[].forEach.call([], () => {})
