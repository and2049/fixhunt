function getConfig() {
  return null;
}
const settings = getConfig() ?? { debug: true };
console.log('settings.debug:', settings.debug);
// After fix: settings = getConfig() → null, then accessing .debug throws
