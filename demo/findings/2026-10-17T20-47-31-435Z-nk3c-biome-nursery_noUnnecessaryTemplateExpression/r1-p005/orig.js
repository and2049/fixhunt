const obj = {
  [`${'key'}${'name'}`]: 'value'
};
console.log('Key exists:', Object.hasOwn(obj, 'keyname'));
console.log('Value:', obj.keyname);
