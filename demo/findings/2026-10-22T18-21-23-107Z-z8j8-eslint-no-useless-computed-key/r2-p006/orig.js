try {
  const obj = {["throw" + "key"]: 1};
} catch (e) {
  console.log(e.name, e.message);
}
