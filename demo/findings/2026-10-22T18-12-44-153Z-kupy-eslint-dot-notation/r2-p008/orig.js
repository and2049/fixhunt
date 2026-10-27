class Base{get p(){return 42;}}
class Der extends Base{get p(){return super['p']*2;}}
console.log(new Der().p);
