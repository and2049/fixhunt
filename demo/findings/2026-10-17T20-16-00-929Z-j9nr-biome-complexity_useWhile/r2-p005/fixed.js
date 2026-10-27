class C { static y = console.log('static') || 1; }
while (C.y) {
  console.log('loop');
  break;
}
