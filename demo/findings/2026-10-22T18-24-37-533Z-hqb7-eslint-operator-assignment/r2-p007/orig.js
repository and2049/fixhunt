let i = 0;
const arr = [0, 0];
arr[i++] = arr[i++] + 1;
console.log(arr[0], arr[1], i); // i incremented twice vs once
