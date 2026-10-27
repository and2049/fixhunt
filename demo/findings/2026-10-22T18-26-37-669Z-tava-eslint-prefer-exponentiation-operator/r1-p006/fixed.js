const obj = {};
obj.__proto__.Math = { pow: (b, e) => b + e };
console.log('obj.Math.pow(2,3):', obj.Math.pow(2, 3));
// Rule would see obj.Math.pow and NOT fire (not direct Math)
// So no rewrite happens here.
console.log('Global Math.pow(2,3):', 2**3);
