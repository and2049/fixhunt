try {
  const jsx = <svg:circle></svg:circle>;
  console.log('parsed', typeof jsx);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
