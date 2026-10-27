try {
  (/[=]/.test(null));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
