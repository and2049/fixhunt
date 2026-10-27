let x = 1;
try {
  eval("switch(x){case 1: const y=2, z=y+1; break}");
} catch(e) {
  if (e instanceof SyntaxError) {
    console.log('SyntaxError as expected');
  } else {
    throw e;
  }
}
