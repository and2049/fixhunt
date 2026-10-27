function tdztest() {
  if (false)
    ; // dummy to avoid warning
  for (var i = 0; i < 1; i++)
    let tmp = i
  console.log(typeof i, typeof tmp)
  var i = 99
}
tdztest()
