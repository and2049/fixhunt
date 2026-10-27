// Hazard 3: Getter called once vs twice
const obj = {
  get prop() {
    console.log('getter called');
    return 'value';
  }
};
console.log('' + obj.prop + obj.prop);
