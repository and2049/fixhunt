// Hazard 7: Label/break/continue
outer: {
  for (let i = 0; i < 2; i++) {
    if (i === 1) break outer;
    const el = `<div className="loop-${i}"></div>`;
    console.log(el);
  }
}
console.log("after break");
// Fix runs but break skips second iteration
