// This comment should stay
import { ref } /* inline */ from "vue"; // trailing
console.log(typeof ref === "function" ? "ok" : "missing");
