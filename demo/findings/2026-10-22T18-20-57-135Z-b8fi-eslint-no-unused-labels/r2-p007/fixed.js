{
  try {
    console.log(letX); // ReferenceError due to TDZ
  } catch (e) {
    console.log(e.name); // ReferenceError
  }
  let letX = 42;
}
