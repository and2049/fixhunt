let o={},id=null;function log(){id=this;return 42;}
Object.defineProperty(o,'val',{get:log,configurable:true});
console.log(o.val,id===o?'bound':'lost');
delete o.val;Object.defineProperty(o,'val',{get:log});
console.log(o.val,id===o?'bound':'lost');
