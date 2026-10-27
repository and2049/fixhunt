try {
  const regex = new RegExp('\\256');
  console.log(regex.test('\xa0'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
