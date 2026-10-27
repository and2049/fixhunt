const STATE = { IDLE: 0b0000, RUNNING: 0b0001, PAUSED: 0b0010, STOPPED: 0b0100 };
let current = STATE.RUNNING | STATE.PAUSED; // 0b0011
if ((current & 0b1010) !== 0) {
  console.log('flag match');
} else {
  console.log('no match');
}
// After fix: 0b1010 becomes 10 → changes bitmask logic
