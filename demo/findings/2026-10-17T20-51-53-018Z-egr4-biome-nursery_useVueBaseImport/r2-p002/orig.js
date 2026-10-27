"use strict";
import { reactive } from "@vue/runtime-core";
try {
  reactive(null);
} catch (e) {
  console.log(e.constructor.name);
}
