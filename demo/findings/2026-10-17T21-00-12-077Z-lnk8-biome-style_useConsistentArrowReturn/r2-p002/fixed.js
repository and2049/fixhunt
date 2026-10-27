let log = '';
const side = (msg) => {
  log += msg;
  return msg.length;
};

// Arrow with comma expression - rule triggers
const getVals = () => (side('a'), side('b'));

const first = getVals();
log += '|';
const second = getVals();
console.log('log:', log);
console.log('first:', first);
console.log('second:', second);
