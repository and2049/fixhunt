let link = document.createElement('link');
link.href = 'https://fonts.gstatic.com';
{ 
  const link = document.createElement('link');
  link.href = 'https://fonts.gstatic.com';
  console.log(link.getAttribute('rel'));
}
link.setAttribute('rel', 'preconnect');
console.log(link.getAttribute('rel'));
