function factory(){return function(){}};
let F = factory();
console.log(F.prototype !== undefined ? 'has' : 'no-proto');
