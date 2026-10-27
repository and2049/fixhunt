export default {
  data: {
    arr: [, 1, , 3]
  }
};
const vm = {};
vm.data = { arr: [, 1, , 3] };
console.log(Object.keys(vm.data.arr).length);
console.log(vm.data.arr.length);
