let x=9;(function(){let x=5;[1,2].map(v=>{console.log('inner',x+v);return x+v;}))();
console.log('outer',x);
