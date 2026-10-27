const regex = /a/g;
const str = 'aa';
let match;
while ((match = regex.exec(str)) !== null) {
  console.log(match.index);
}
// After fix: let → const, but regex still mutable via lastIndex
console.log('done');
