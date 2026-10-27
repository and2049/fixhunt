// Hazard 6: Comment on the line with await
// This comment should stay after fix
await { click: () => console.log('hi') }.click(); // keep this comment
console.log('After');
