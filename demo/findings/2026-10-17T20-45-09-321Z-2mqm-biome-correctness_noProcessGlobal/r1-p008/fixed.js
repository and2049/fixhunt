import process from "node:process";
switch (1) {
  case 1:
    function process() { return 'func'; }
    console.log(process());
    break;
}
console.log(typeof process);
