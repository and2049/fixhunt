import { isRef } from "@vue/shared";
const obj = {};
Object.defineProperty(obj, "value", {
  get: () => isRef({}) ? 1 : 0
});
console.log(obj.value);
