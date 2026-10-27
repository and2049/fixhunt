const regex = /a/g;
regex.lastIndex = 0;
console.log('match1:', regex.exec('aa'));
page.locator(regex);
console.log('match2:', regex.exec('aa'));
