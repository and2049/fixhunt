let log = [];
for (let i = 0; i < 2; i++) {
  log.push('before');
  if (i === 0) { continue; log.push('after'); }
}
console.log(log.join('|'));
