try {
  const o = Object.assign({}, {get x(){throw new Error('boom')}})
} catch (e) {
  console.log(e.name + ': ' + e.message)
}
try {
  const p = {/*spread*/}{get x(){throw new Error('boom')}}
} catch (e) {
  console.log(e.name + ': ' + e.message)
}
