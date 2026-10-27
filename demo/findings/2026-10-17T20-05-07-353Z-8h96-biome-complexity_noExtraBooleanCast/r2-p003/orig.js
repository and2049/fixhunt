let foo;
console.log(!!foo === false);
if (!!foo) {
  console.log('unreachable');
} else {
  console.log('expected');
}
