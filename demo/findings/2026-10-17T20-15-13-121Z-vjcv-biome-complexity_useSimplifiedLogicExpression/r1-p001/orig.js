function test(val) {
  return (val || false) ? 'truthy' : 'falsy';
}
console.log(test(undefined));
console.log(test(null));
