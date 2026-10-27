let v = undefined;
console.log(!!v ?? 'default');
v = null;
console.log(!!v ?? 'default');
