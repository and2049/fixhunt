class C { static y = console.log('static') || 1; }
for (; C.y;) {
  console.log('loop');
  break;
}
