const arr = Array(3)
advanced: {
  arr[0] = 0b10
  arr[2] = 0o10
  console.log(arr.map((v, i) => v !== undefined ? v : 'hole'))
}
