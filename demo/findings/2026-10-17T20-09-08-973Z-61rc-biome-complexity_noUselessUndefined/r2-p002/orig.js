function F() {
  this.x = 1;
  return undefined;
}
let o1 = Reflect.construct(F, [], F);
console.log(o1.x);
function G() {
  this.x = 2;
  return;
}
let o2 = Reflect.construct(G, [], G);
console.log(o2.x);
