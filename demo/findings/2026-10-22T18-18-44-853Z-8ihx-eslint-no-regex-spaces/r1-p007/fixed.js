let re = /\s+ {2}\d+/gu;
re.lastIndex = 0;
let m1 = re.exec('a  5');
let m2 = re.exec('a  5');
console.log(m1 ? m1.index : -1, m2 ? m2.index : -1);
