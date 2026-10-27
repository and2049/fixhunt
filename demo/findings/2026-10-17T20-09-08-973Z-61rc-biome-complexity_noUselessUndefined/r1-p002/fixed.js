let callLog = [];
function sideEffect(){
  callLog.push('init');
  return ;
}

function f(a = sideEffect()){ // rule triggers here
  callLog.push('body: ' + (a === undefined ? 'undef' : 'def'));
}

f();           // triggers default param init
f(undefined);  // does NOT trigger default param init

console.log(callLog.join(' | '));
