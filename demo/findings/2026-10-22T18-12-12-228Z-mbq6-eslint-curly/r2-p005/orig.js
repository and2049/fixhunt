function h(...args) {
  let fns = []
  for (let i = 0; i < args.length; i++)
    fns.push(() => args[i])
  return fns.map(fn => fn())
}
console.log(h(10, 20))
