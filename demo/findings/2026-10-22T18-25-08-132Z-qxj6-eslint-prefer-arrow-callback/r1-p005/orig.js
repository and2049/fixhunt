const obj={value:42,getValue:function(){return this.value;}};
const fn=obj.getValue;
console.log('direct:',obj.getValue());
console.log('call:',fn.call(obj));
console.log('bind:',fn.bind(obj)());
