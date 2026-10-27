(function(){
  'use strict';
  let strictLog = '';
  const strictFn = () => { return strictLog += 's'; };
  strictFn();
  console.log('strict:', strictLog);
})();

(function(){
  // sloppy mode
  let sloppyLog = '';
  const sloppyFn = () => { return sloppyLog += 'S'; };
  sloppyFn();
  console.log('sloppy:', sloppyLog);
})();
