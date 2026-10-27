
const STATE_FLAGS = { READY: 0b0001, PROCESSING: 0b0010, SUCCESS: 0b0100, FAILURE: 0b1000 };
const stateObj = { 0b1010: 'composite' }; // 0b1010 = PROCESSING | SUCCESS
let flags = STATE_FLAGS.PROCESSING | STATE_FLAGS.SUCCESS;
console.log(stateObj[flags] === 'composite' ? 'match' : 'no match');
