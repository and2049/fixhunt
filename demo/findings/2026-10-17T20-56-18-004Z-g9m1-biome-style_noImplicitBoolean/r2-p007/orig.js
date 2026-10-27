// Hazard 7: __proto__ and prototype access
const base = { disabled: false };
const obj = { __proto__: base, disabled: true };
console.log('obj.disabled:', obj.disabled);
// Rule fires here - reading property that may come from prototype
const el = <input disabled={obj.disabled} />;
console.log('after JSX, obj.disabled:', obj.disabled);
