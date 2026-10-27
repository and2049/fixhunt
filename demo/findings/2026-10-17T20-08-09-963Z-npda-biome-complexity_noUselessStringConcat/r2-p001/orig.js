const obj = { get prop() { console.log('getter'); return 'X'; } };
let result = '' + obj.prop + '' + obj.prop;
console.log(result);
