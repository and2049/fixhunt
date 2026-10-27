import settings from './data.json' with { type: "json" };
const value = settings?.nested ?? 'default';
console.log(value);
