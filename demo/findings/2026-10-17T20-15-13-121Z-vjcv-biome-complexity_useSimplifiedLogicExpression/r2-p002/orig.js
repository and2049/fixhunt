for (let i = 0; i < 2; i++) {
  try {
    true && var x = i;
    console.log(x);
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
}
