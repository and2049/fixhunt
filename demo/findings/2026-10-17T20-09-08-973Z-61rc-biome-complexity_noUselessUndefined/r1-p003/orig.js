let result = [];
function test(val){
  result.push(String(val));
}

// Hazard: default in parameter destructuring
function g({a = undefined}){
  test(a);
}

g({a: null});   // should preserve null -> logs 'null'
g({a: undefined});// logs 'undefined'
g({});          // missing -> default -> logs 'undefined'

g = null;       // redeclaration after use

console.log(result.join(' | '));
