export default {
  data: Object.freeze({ x: 1 })
};
const frozen = Object.freeze({ x: 1 });
const vm = {};
vm.data = frozen;
try {
  vm.data.x = 2;
} catch (e) {
  console.log(e.name);
}
console.log(vm.data.x);
