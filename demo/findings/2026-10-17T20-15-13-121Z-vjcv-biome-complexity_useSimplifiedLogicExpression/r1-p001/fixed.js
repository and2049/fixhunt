function test(val) {
  return (val) ? 'truthy' : 'falsy';
}
console.log(test(undefined));
console.log(test(null));
