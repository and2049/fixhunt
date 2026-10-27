// Binary string representing 2^53 + 1
const s = '1' + '0'.repeat(53) + '1'; // 1000...001 (54 bits)
console.log('parseInt:', parseInt(s, 2));
// This triggers prefer-numeric-literals: rewrite to 0b1000...001
// But 0b1000...001 > Number.MAX_SAFE_INTEGER, so literal loses precision
console.log('literal attempt:', 0b1000000000000000000000000000000000000000000000000000001);
console.log('Are they equal?', parseInt(s, 2) === 0b1000000000000000000000000000000000000000000000000000001);
