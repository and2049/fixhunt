function get() { return ++counter; }
let counter = 0;
console.log(get(), get());
counter = 0;
{ const temp = get(); console.log(temp, temp); }
