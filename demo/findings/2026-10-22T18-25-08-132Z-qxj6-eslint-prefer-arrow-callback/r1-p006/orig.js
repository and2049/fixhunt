function makeCtor(){return function Custom(){this.x=1;}};
let C=makeCtor();try{let i=new C();console.log('ok',i.x);}catch(e){console.log(e.name,e.message);}
