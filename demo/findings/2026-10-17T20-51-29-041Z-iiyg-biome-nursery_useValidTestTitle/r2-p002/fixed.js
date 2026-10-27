const levels = ['unit', 'integration', 'e2e'];
levels.forEach(level => {
  describe(`  ${level.toUpperCase()}  `, () => {
    // Intentionally padded for column-aligned test output
    console.log(`[${level}] suite entered`);
    it(`  ${level}-test  `, () => {
      console.log(`  -> ${level} test ran`);
    });
  });
});
