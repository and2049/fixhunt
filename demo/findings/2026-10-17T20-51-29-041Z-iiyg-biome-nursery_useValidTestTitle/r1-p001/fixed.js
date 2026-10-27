// Comment above
function test(title, cb) {
  return cb ? cb(title) : title;
}
let result = '';
result += test(/* title */ 123, x => { result += x; });
console.log(result);
