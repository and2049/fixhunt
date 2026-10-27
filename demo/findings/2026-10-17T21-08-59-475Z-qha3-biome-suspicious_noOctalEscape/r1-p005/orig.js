const s = "\377"; // intended as byte 255
const utf8 = new TextEncoder().encode(s);
console.log(utf8.length, '[', utf8.join(','],]');
