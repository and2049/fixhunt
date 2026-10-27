const s = 'ab';
console.log(Object.assign({}, s).0, Object.assign({}, s).length)
console.log({...s}.0, {...s}.length)
const symObj = {[Symbol.for('test')]: 42};
console.log(Object.assign({}, symObj)[Symbol.for('test')])
console.log({...symObj}[Symbol.for('test')])
