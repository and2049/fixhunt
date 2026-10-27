"use strict";
outer: {
  for (let i = 0; i < 3; i++) {
    if (i === 1) break outer;
    try {
      console.log(parseInt(String(i)));
    } finally {
      console.log('finally');
    }
  }
}
