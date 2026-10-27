// Hazard 1: Spread operator with conflicting className
const props = { className: "spread-class", id: "test" };
function render() {
  return `<div ${{"{...props}"}} className="explicit-class">content</div>`;
}
console.log(render());
