
const PERMS = { OWNER_READ: 0o400, GROUP_READ: 0o040, OTHERS_READ: 0o004 };
const config = { 0o755: 'rw-r-xr-x' }; // rewritten to 493
const expected = PERMS.OWNER_READ | PERMS.GROUP_READ | PERMS.OTHERS_READ;
console.log(config[expected] === 'rw-r-xr-x' ? 'semantic match' : 'broken');
