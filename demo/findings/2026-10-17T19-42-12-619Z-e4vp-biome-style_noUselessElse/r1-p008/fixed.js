function main() {
  switch (0) {
    case 0:
      if (false) { return; }
      function g() { return 2; } 
      console.log(typeof g);
      break;
  }
}
main();
