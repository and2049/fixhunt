function process({ data = this }) {
  return data;
}
console.log(process.call({value: 42}, {}));
