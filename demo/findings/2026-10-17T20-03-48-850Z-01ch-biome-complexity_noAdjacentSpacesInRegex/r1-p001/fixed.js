const input = 'a  bc';
let result;
if ((/(a) {2}(bc)/).test(input)) {
  result = RegExp.$1 ?? 'no';
} else {
  result = undefined;
}
console.log(result);
