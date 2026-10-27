let x = /'hello   world'/
(['a','b']).forEach(c => { if (/^h/.test(c)) x = null })
