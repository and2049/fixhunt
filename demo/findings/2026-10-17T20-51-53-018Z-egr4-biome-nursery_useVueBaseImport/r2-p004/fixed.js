import { watch } from "vue";
async function test() {
  await Promise.resolve();
  return watch(() => 1, () => {});
}
test().then(r => console.log(typeof r === "function" ? "stop" : "bad"));
