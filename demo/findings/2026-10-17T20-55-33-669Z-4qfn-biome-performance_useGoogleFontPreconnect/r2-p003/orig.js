const condition = true;
const element = <link href="https://fonts.gstatic.com" rel={condition ? 'preload' : ''} />;
console.log(element.props.rel)
