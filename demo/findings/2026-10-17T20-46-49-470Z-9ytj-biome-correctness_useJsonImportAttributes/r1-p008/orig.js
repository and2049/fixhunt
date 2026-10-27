// Simulated macro: expects import without assertions
const macroProcessed = (() => {
  try {
    import raw from './data.json';
    return typeof raw === 'object' && raw !== null;
  } catch (e) {
    return false;
  }
})();
console.log(macroProcessed);
