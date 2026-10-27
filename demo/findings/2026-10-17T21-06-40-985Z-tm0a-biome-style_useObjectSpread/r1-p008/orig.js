start: {
  if (true) {
    function helper() {
      return Object.assign({}, {flag: true})
    }
    const h = helper()
    console.log(h.flag)
    break start
  }
  switch (0) {
    case 0:
      function caseFn() {
        return Object.assign({}, {case: 0})
      }
      console.log(caseFn().case)
      break
  }
}
