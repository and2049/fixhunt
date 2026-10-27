{ 
  try {
    console.log(Object.hasOwn(value, 'a'));
  } catch (e) {
    console.log(e.name, e.message);
  }
  const value = {};
}
