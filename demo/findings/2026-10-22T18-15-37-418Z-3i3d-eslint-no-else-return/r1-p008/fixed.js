function protoTest(obj) {
  if ('__proto__' in obj) {      // Trigger: proto check
    return obj.__proto__;        // Returns prototype
  }                              
                           // Hazard: else block
    obj.custom = 'added';        // Mutates input
    return obj;                  
  
}
const map = { a: 1 };
console.log('before:', map.custom);
const result = protoTest(map);   // Modifies map
console.log('after:', map.custom);
console.log('result:', result.custom);
