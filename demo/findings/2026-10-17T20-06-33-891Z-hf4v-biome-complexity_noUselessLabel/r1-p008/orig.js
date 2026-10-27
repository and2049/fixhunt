let exportedValue = 42;
outer: {
  eval('exportedValue = 99;');
  break outer;
}
console.log('exportedValue:', exportedValue);
