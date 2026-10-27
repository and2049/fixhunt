const re = /^ {2}(\d{3}) {2}- {2}(\d{2}) {2}- {2}(\d{4})$/;
const m = '123-45-6789'.match(re);
console.log(m ? m[1] + '-' + m[2] + '-' + m[3] : null);
