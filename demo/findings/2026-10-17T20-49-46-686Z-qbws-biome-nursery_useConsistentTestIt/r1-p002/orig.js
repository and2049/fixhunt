import { test as runner } from 'assert';
try {
  runner.ok(true, 'pass');
  console.log('Assertion passed');
} catch (e) {
  console.log(`Error: ${e.name}`);
}
