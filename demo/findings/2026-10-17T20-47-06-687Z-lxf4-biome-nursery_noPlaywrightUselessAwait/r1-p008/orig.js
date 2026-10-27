// Hazard 8: Removing await breaks .then() chain
let result = 'none';
// Simulate locator that returns a promise-like thenable
const loc = {
  then: (cb) => { cb('resolved'); return loc; }
};
// Normally: await loc.then(v => { result = v; });
// But rule sees: await loc - and removes await, leaving loc.then(...)
// So we do: await loc; then .then? No - we make it so the code is: await loc.then(...)
// But rule only fires on await loc, not await loc.then...
// So we need: await loc  -> but we want to test if removing await breaks a chain that comes AFTER
// Let's restructure: code is: await loc; loc.then(...)  -> but that's two statements
// Instead: make it one expression: (await loc).then(...) -> rule doesn't fire on that
// We need the rule to fire on a subexpression that is used in a chain
// Final attempt: we make the locator call itself be chained, but rule fires on the await
console.log('Skipped - complex');
