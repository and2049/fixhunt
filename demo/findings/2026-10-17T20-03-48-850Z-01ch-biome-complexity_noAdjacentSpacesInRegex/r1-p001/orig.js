const input = 'a  bc';
let result;
if ((/(a)  (bc)/).test(input)) {
  result = RegExp.$1 ?? 'no';
} else {
  result = undefined;
}
console.log(result);
