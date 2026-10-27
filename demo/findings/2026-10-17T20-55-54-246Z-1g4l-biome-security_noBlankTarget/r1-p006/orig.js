function SafeLink({target, rel, ...rest}) {
  return <a {...rest} target={target} rel={rel}>link</a>;
}
const el = <SafeLink target="_blank" href="/url" />;
console.log('Wrapper got rel?', !!el.target);
