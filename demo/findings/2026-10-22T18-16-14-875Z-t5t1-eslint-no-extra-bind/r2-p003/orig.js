const log = (function () {
  console.log('no this used');
}).bind(undefined); // preserve comment
console.log(typeof log);
