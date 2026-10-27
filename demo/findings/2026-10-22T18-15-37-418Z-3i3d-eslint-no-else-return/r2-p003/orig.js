try {
  if (false) { return 1; }
  else { break; }
} catch (e) {
  console.log(e.name + ":" + e.message);
}
