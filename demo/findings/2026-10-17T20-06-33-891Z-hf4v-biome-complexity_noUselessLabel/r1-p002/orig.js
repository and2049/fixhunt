let lbl = 99;
{
  lbl: {
    console.log('lbl var:', lbl);
    break lbl;
  }
}
console.log('after:', lbl);
