// Hazard 5: Side effect in argument runs twice if await removed and expr duplicated
let count = 0;
const getArg = () => { count++; return '.el'; };
// Rule sees: await page.locator(getArg()) - if it duplicates the call...
{ const l = { click: () => console.log('count', count) }; await l.click(); }
// We simulate: if await removed and expr duplicated, getArg might run twice
// But we can't duplicate - so we make the hazard visible by having the call itself have side effect
console.log('Final count:', count); // Should be 1 if await kept, but we show it's used
