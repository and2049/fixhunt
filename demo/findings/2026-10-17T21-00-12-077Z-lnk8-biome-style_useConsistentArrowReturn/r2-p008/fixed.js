(function(){
  'use strict';
  let strictLog = '';
  const strictFn = () => strictLog += 's';
  strictFn();
  console.log('strict:', strictLog);
})();

(function(){
  // sloppy mode
  let sloppyLog = '';
  const sloppyFn = () => sloppyLog += 'S';
  sloppyFn();
  console.log('sloppy:', sloppyLog);
})();
