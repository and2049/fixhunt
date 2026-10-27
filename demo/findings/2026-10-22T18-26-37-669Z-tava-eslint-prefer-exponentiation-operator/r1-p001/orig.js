let result;
try {
  // Comment attached after dot
  result = Math//comment
          .pow(2, 3);
  console.log('Success:', result);
} catch (e) {
  console.log('Error:', e.name, e.message);
}
