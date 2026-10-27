let Base = class AValue {};
let Derived = eval('class extends ' + Base.name + ' {}');
console.log(new Derived() instanceof Base ? 'ok' : 'fail');
