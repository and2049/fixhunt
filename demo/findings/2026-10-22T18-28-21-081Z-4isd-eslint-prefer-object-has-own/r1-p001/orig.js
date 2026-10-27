let a = 0, b = 0;
function next() { return ++a; }
function val() { return ++b; }
console.log(Object.prototype.hasOwnProperty.call({ [val()]: 'x' }, next()) ? 'yes' : 'no');
console.log(`a=${a} b=${b}`);
