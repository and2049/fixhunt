let val = 0;
const obj = {
  get prop(){ return val; },
  set prop(v){ val = v; log.push('set:' + v); }
};
let log = [];
obj.prop += '';
console.log(log.join('|'), val);
