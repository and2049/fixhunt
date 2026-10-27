(() => {
  let log = [];
  const f = v => { log.push(v); return v; };
  let a = f(1), b , c = f(2); // Rule triggers on b
  console.log(log.join(','));
})();
