const map = {}
Object.defineProperty(map, '__proto__', {
  set(v) { console.log('proto set to:', v) }
})
map.__proto__ = { parseInt: (s, r) => parseInt(s, r) + 100 }
console.log(map.parseInt('10', 2))
