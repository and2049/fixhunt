let called = 0;
export default {
  data: {
    get value() {
      called++;
      return called;
    }
  }
};
const vm = {};
vm.data = { get value() { called++; return called; } };
console.log(vm.data.value);
console.log(vm.data.value);
