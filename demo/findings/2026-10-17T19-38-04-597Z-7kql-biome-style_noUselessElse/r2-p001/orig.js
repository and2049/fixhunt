function f() {
  if (true)
    return
  []
  console.log('unreachable')
}
f()
