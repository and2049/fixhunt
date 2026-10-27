let fallbackUsed = false;
const getValue = () => {
  fallbackUsed = true;
  return null;
};
try {
  const proto = getValue() || false;
  Object.defineProperty({}, '__proto__', { value: proto });
} catch (e) {
  console.log('Error:', e.name, fallbackUsed ? '(fallback used)' : '(no fallback)');
}
