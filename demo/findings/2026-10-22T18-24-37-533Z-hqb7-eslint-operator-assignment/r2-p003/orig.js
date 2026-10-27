const obj = {
  get prop() {
    console.log('get');
    return 5;
  }
};
obj.prop = obj.prop + 1; // getter called twice originally
