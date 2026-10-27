const line = 'a\tb\tc';
const re = /\t  \t/;
console.log('TSV match:', re.test(line));
console.log('Expected fields:', line.split('\t'));
