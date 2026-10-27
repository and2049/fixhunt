let obj = { foo: undefined };
if (obj?.foo ?? false) {
  return;
} else {
  console.log(obj?.foo ?? 'default');
}
