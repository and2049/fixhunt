let value = 'blue';
if (false && ("red" == value)) {
  console.log('unreachable');
} else {
  console.log('false path');
}
// Rule triggers on parenthesized form
if (false && (value == "red")) {
  console.log('also unreachable');
} else {
  console.log('false path 2');
}
