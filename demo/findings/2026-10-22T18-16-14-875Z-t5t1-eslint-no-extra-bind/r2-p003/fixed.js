const log = (function () {
  console.log('no this used');
}); // preserve comment
console.log(typeof log);
