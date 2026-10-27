// this comment must survive the fix
if (false) {
  // empty then
} else {
  // comment kept only if else remains
  console.log('else body');
}
// after fix the comment may be lost or the else removed entirely
print('program end');
