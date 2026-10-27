// This comment should stay
import { ref } /* inline */ from "@vue/reactivity"; // trailing
console.log(typeof ref === "function" ? "ok" : "missing");
