const val = eval('__dirname');
console.log('eval result:', typeof val === 'string' && val.length > 0 ? 'defined' : 'undefined');
console.log('import.meta.dirname:', typeof import.meta.dirname === 'string' ? 'defined' : 'undefined');
