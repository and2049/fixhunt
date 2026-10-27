let seq = []
const obj1 = {get a(){seq.push(1); return 1}}
const obj2 = {get b(){seq.push(2); return 2}}
const res = ({...obj1,...obj2,})
console.log('seq:', seq.join(', '), 'res:', JSON.stringify(res))
