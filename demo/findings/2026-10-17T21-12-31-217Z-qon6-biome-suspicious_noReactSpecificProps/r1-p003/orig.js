const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.setAttribute('className', 'test'); // sets attribute
console.log(svg.getAttribute('class'));
// After fix: becomes <svg class="test" ...> -> getAttribute('class') returns null because attribute is now 'class'
// But we simulate by checking what the parser sees:
console.log(svg.hasAttribute('className')); // false after fix? Actually we set className manually.
// Instead, show that accessing .className property on SVGElement returns string (reflects class)
console.log(typeof svg.className);
