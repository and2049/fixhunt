switch(1) {
  case 1:
    function g(){ return 1; }
    console.log(g());
    break;
}
try {
  import { h } from './mod.js'; // mod.js does not export h
} catch(e) {
  console.log(e.code);
}
