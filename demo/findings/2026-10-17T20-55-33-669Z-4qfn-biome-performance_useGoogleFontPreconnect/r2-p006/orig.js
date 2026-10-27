const obj = {
  get link() {
    return '<link href="https://fonts.gstatic.com" />';
  }
};
const getLink = obj.link;
console.log(getLink())
