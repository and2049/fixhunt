const obj = {val: 42, getNum(){ return +this.val; }};
const fn = obj.getNum;
try{ console.log(fn.call(obj)); }catch(e){ console.log(e.name); }
