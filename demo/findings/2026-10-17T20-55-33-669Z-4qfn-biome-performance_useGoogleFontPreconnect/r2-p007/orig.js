const regex = /https:\/\/fonts\.gstatic\.com/g;
const str = '<link href="https://fonts.gstatic.com"/> <link href="https://fonts.gstatic.com"/>;
let match;
while ((match = regex.exec(str)) !== null) {
  console.log(match.index);
}
