for (var i = 0; i < 2; i++) {
  if (typeof process === 'undefined') console.log('undef');
  else console.log(process.version);
  var process = { version: 'loop' + i };
}
