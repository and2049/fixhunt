start: {
  if (true) {
    function helper() {
      return ({flag: true,})
    }
    const h = helper()
    console.log(h.flag)
    break start
  }
  switch (0) {
    case 0:
      function caseFn() {
        return ({case: 0,})
      }
      console.log(caseFn().case)
      break
  }
}
