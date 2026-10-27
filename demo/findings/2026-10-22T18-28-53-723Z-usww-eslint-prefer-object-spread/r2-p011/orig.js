const arr = Array(3);
arr[1] = 'a';
console.log('assigned:', Object.assign({}, arr));
console.log('spread:', { ...arr });
arr.toString = () => 'custom';
console.log('String assigned:', String(Object.assign({}, arr)));
console.log('String spread:', String({ ...arr }));
