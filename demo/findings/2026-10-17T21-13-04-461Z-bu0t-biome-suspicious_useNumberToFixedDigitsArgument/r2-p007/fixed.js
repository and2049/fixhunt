let i = 0;
const getObj = () => ({
  toFixed: () => {
    return i++;
  }
});
console.log(getObj().toFixed() + ', ' + getObj().toFixed());
