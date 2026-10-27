(() => {
  const log = [];
  const regex = /a/g;
  regex.lastIndex = 0;
  // Hazard: condition uses regex.test() which advances lastIndex
  if (regex.test('aa')) { log.push(regex.lastIndex); } else { log.push('if'); }
  // After fix: condition becomes regex.test('aa') -> true, so else runs
  console.log(log.join('|')); // Before fix: 'if'; after fix: '1'
})();
