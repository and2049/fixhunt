let obj = null;
try {
  if (null == obj?.prop) console.log('matched');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
obj = {prop: null};
if (null == obj?.prop) console.log('matched');
