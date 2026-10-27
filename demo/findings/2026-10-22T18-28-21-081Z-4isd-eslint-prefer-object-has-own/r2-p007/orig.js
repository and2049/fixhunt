let o = {a: 1};
if (Object.prototype.hasOwnProperty.call(o, 'a')) { // check if a exists
  console.log('yes');
} // end if
console.log('done');
