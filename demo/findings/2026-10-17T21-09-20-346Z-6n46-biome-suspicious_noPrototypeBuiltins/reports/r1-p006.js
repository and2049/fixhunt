const fakeAll = { 
};
fakeAll.__proto__ = null;
try {
  console.log(fakeAll == null, fakeAll.hasOwnProperty('length'));
} catch (e) {
}
