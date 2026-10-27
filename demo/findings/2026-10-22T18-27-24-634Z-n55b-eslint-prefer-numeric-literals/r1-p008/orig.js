let o = { ['__proto__']: parseInt('111110111', 2) }; console.log(o.__proto__ === Number.prototype ? 'Number' : 'other');
