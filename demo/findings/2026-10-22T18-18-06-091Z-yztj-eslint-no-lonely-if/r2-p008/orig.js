const cond = false;
const html = cond
  ? '<div>yes</div>'
  : (() => {
      if (true) return '<span>no</span>';
      return '';
    })();
console.log(html);
