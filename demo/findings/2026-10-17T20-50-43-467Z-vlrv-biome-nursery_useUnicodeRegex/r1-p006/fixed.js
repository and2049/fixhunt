let count = 0;
let getPat = () => {
  count++;
  return 'a';
};
let r = new RegExp(getPat(), 'u');
console.log(count);
