try {
  const val = parseInt('0x12', 16)
  console.log(val === 0x0x12 ? 'rewritten' : val)
} catch (e) {
  console.log(e.name + ': ' + e.message)
}
