// Hazard 3: __proto__ tampering affects object shape
const base = { locator: () => ({ click: () => console.log('real') }) };
const fake = { __proto__: base, locator: () => ({ click: () => console.log('fake') }) };
// Rule sees: await fake.locator() -> but __proto__ may interfere
{ const l = fake.locator(); await l.click(); }
{ const l = fake.locator(); l.click(); } // No await - still works? but we test if rule fires
console.log('Test done');
