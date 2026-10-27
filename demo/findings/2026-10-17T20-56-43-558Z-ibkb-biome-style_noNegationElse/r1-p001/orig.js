(() => {
  const log = [];
  try {
    // Hazard: 'let' declared in condition scope
    if (!let x = 1) { log.push('if'); } else { log.push(x); }
  } catch (e) {
    log.push(e.name + ': ' + e.message);
  }
  console.log(log.join('|'));
})();
