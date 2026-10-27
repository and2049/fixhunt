const arr = [10, 20, 30];
let idx = 0;
arr[idx++] = arr[idx++] + 5; // TRIGGER: idx read twice
console.log('idx after:', idx, 'arr:', arr);
// Reset
idx = 0;
arr[idx++] = arr[idx++] + 5; // Same line again
console.log('idx after2:', idx, 'arr2:', arr);
