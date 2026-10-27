const obj = {
  valueOf() { return 0; }
};
if (!!obj) console.log('truthy'); else console.log('falsy');
