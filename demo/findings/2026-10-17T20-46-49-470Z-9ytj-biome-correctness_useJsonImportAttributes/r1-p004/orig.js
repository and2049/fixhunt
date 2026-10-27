import settings from './data.json';
const value = settings?.nested ?? 'default';
console.log(value);
