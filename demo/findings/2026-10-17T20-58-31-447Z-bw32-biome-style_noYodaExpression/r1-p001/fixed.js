let obj = null;
try {
  if (obj?.prop == null) console.log('matched');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
obj = {prop: null};
if (obj?.prop == null) console.log('matched');
