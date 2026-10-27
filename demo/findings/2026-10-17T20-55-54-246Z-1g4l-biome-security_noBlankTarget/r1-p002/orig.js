function Link({href, target}) {
  return <a href={href} target={target}>click</a>;
}
const el = <Link href="/url" target="_blank" />;
console.log('Component rendered');
