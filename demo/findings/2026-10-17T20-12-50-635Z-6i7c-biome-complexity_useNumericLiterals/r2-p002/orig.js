const arr = Array(3)
advanced: {
  arr[0] = parseInt('10', 2)
  arr[2] = parseInt('10', 8)
  console.log(arr.map((v, i) => v !== undefined ? v : 'hole'))
}
