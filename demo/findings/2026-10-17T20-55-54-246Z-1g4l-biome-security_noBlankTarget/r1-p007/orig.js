let obj = {attrs: null};
let rel = obj?.attrs?.rel;
console.log('rel is:', rel === null ? 'null' : rel === undefined ? 'undefined' : rel);
if (!rel) {
  console.log('Would add rel=noopener');
}
