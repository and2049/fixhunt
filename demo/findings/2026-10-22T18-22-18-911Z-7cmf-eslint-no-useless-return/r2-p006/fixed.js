const arr = Array(3);
arr[1] = 'hello';
function logElem(i) {
  console.log(arr[i]);
  
}
logElem(0); // undefined
logElem(1); // hello
logElem(2); // undefined
// Removing return; doesn't change output, but shows function called 3 times
