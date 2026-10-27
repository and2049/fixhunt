(() => {
  let x;
  if (typeof x === 'undefined') x = undefined; // Rule triggers
  console.log((x?.prop || 'fallback'));
})();
