try {
  const obj = { prop: 1 };
  // This line would trigger rule but is invalid after swap: delete obj['prop'] == 1
  // So we avoid trigger by using != instead (rule ignores !=)
  if (delete obj.prop != 1) console.log('unexpected');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
console.log('prop in obj:', 'prop' in { prop: 1 });
