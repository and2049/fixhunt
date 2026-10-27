try {
  const regex1 = new RegExp('\\1');
  console.log('Pattern without u:', regex1);
  console.log('Test "\\x01"\\x01:', regex1.test('\x01\x01'));
} catch (e) {
  console.log('Error:', e.name + ': ' + e.message);
}
try {
  const regex2 = new RegExp('\\1', 'u');
  console.log('Pattern with u:', regex2);
  console.log('Test "\\x01"\\x01:', regex2.test('\x01\x01'));
} catch (e) {
  console.log('Error with u:', e.name + ': ' + e.message);
}
