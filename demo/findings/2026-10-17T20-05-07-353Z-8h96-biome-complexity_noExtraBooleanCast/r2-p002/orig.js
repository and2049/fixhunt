const str = 'aa';
const re = /a/g;
let m;
while (!!(m = re.exec(str))) {
  console.log(m.index, re.lastIndex);
}
