let result = ''
(() => {
  if (!foo)
    result += 'A'
  else
    result += 'B'
})()
