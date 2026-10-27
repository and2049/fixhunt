const str = 'ÁxÁy';
const parts = str.split(/[Á]/);
console.log(parts.length, parts); // 3 [ '', 'x', 'y' ]
// After fix: split by /[A]/ -> no match, so ['ÁxÁy']
console.log(str.split(/[A]/).length, str.split(/[A]/)); // 1 [ 'ÁxÁy' ]
