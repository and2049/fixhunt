for (var i = 0; i < 2; i++) {
  var { z: z } = { z: i * 10 };
  if (i === 1) console.log(z); // Should be 10 after second iteration
  var { z: z } = { z: 99 }; // Redeclaration
}
