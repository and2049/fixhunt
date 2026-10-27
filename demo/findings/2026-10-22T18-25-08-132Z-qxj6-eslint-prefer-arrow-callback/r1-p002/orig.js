let x=1,y=2,z=0;
x + y * z === 1 ? console.log('A') : console.log('B',x+y*z);
(function(){z=x+y;})();
console.log(z);
