let flag = false;
console.log(true == flag ? 'yes' : 'no'); // triggers yoda
// After fix: flag == true -> same result
flag = true;
console.log(true == flag ? 'yes' : 'no');
