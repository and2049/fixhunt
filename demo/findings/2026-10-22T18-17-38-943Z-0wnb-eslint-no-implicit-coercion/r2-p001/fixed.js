let obj = new Proxy({ valueOf: () => { console.log('valueOf'); return 42; }, toString: () => { console.log('toString'); return '42'; } }, {});
console.log(+obj);
console.log(Boolean(obj));
