"use strict";
import { reactive } from "vue";
try {
  reactive(null);
} catch (e) {
  console.log(e.constructor.name);
}
