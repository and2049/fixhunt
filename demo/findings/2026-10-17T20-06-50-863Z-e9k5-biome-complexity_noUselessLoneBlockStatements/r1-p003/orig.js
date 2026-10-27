try {
  ({}).toString();
} catch (e) {
  console.log(e.name, e.message);
}
