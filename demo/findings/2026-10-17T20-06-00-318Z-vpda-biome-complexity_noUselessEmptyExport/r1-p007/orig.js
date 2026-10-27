(async () => {
  await Promise.resolve();
  var local = 'safe';
  export {};
  console.log(typeof local === 'string' && !globalThis.local);
})();
