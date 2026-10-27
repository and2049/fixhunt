(() => {
  let log = [];
  const f = v => { log.push(v); return v; };
  let a = f(1), b = undefined, c = f(2); // Rule triggers on b
  console.log(log.join(','));
})();
