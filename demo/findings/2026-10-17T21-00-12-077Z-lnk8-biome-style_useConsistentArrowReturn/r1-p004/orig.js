switch (1) {
  case 1:
    let x = 10;
    const getX = () => { return x; };
    break;
}
try {
  console.log(getX());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
