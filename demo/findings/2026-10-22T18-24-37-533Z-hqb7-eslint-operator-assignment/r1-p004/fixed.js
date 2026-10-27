let counter = 0;
counter = counter /* step */ + 1; // TRIGGER
console.log('after first:', counter);
counter = counter /* inline */ + counter; // TRIGGER
console.log('after second:', counter);
