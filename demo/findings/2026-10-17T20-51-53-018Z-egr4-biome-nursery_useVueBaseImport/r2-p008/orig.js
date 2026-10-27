import { ref } from "@vue/reactivity";
const arr = new Array(3);
arr[0] = ref(0);
arr[2] = ref(2);
console.log(arr.map((v, i) => v ? `has${i}` : `hole`));
