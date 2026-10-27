/* start */
let r = /a/* middle */;
let m = r.exec('a');
console.log(m ? m[0] : null);
/* end */
