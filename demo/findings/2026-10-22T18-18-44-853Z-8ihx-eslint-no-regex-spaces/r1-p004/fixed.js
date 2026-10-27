let x = /'hello {3}world'/
(['a','b']).forEach(c => { if (/^h/.test(c)) x = null })
console.log(x === null ? 'failed' : x.source)
