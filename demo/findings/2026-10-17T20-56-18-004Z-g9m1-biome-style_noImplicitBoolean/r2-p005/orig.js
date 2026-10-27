// Hazard 5: Label/break/continue with finally
outer: {
  try {
    // Rule fires below
    const el = <div hidden />;
    break outer;
  } finally {
    console.log('finally ran');
  }
}
console.log('after outer');
