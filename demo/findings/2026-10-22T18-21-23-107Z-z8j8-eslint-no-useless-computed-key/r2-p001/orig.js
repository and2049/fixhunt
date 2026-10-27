class C {
  ["constructor"] = () => {
    console.log('field called');
    return 'field';
  };
  constructor() {
    this["constructor"](); // calls the field method
    console.log(this.constructor === C); // should be true
  }
}
const c = new C();
