let nextTick = "outer";
{
  import { nextTick } from "@vue/runtime-dom";
  console.log(nextTick === "outer" ? "shadowed" : typeof nextTick);
}
