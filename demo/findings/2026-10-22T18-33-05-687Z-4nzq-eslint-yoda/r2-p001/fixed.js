let flag = false;
console.log(flag == true ? 'yes' : 'no'); // triggers yoda
// After fix: flag == true -> same result
flag = true;
console.log(flag == true ? 'yes' : 'no');
