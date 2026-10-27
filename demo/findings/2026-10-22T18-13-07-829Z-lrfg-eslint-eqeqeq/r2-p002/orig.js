const obj = { get a() { return console.log('get a'), 1 }, get b() { return console.log('get b'), 2 } }
if (obj.a == obj.b) console.log('match')
else console.log('no match')
