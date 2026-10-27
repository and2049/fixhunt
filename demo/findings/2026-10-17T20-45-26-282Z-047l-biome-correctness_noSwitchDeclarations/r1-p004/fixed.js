function check(value) {
  switch(typeof value) {
    case 'object': {
      const data = value?.prop?.sub;
      if (data == null) throw 'nullish';
      return data;
    }
    default:
      return undefined;
  }
}
try {
  console.log(check(null));
} catch(e) {
  console.log('Caught:', e);
}
