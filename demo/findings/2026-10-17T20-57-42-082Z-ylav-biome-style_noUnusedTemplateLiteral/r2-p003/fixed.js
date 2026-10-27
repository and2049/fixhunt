let s = "a\`b"; // Template literal containing escaped backtick
console.log(s); // Should print: a`b
// After fix: becomes 'a`b' → invalid due to unescaped backtick in single quotes
