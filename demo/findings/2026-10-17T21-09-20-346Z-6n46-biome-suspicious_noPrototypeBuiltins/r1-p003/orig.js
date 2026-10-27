{ 
  try {
    console.log(value.hasOwnProperty('a'));
  } catch (e) {
    console.log(e.name, e.message);
  }
  const value = {};
}
