Z: function(a, b = 1, ...rest) {
  console.log(arguments.length, b, rest.length);
  break Z;
}(5)
console.log('done');
