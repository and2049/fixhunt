// Hazard 4: Escaping in template literals - no issue expected
const path = `C:\\Users\\name` + `\\file.txt`;
console.log(path);
