class C {
  flag = (this.value || false);
  constructor() {
    this.value = undefined;
  }
}
const c = new C();
console.log('flag:', c.flag);
// After fix: flag = this.value → undefined
