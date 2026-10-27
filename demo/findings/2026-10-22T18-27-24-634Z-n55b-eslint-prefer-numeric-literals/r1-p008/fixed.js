let o = { ['__proto__']: 0b111110111 }; console.log(o.__proto__ === Number.prototype ? 'Number' : 'other');
