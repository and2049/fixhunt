LOOP: {
  try {
    console.log((function () {
      for (let i = 0; i < 3; i++) {
        if (i === 1) continue LOOP;
        if (i === 2) return;
      }
      console.log('reached');
    }).bind(null));
    throw new Error('unreachable');
  } catch (e) {
    console.log(e.message);
  } finally {
    console.log('finally executed');
  }
}
