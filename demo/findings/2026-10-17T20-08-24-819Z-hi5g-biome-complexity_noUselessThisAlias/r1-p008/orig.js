let self = this;
self.data = [10, , 30];
const result = Array.from({length: 3}, (_, i) => self.data[i] ?? -1);
console.log(result.join(','));
