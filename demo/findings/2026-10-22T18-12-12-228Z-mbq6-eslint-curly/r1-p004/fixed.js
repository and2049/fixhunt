const obj = {};
for (let k of ['a', '__proto__'])
  {if (k === '__proto__')
    {obj[k] = { toString: () => 'hijacked' };}}
console.log(obj.toString());
