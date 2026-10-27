let calls=0;function getObj(){calls++;return {x:42};}
console.log(getObj().x,calls);getObj().x+=1;console.log(calls);
