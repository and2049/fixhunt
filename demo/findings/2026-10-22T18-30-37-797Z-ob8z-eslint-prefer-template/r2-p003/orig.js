let log = '';
const getA = () => { log += 'a'; return 'A'; };
const getB = () => { log += 'b'; return 'B'; };
console.log(getA() + (getB(), log += 'side', getB()) + '': log);
