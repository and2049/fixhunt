outer:
for (let i = 0; i < 1; i++) {
  export default {
    data: {
      x: (() => { break outer; return 1; })(),
      y: 2
    }
  };
}
console.log('escaped');
