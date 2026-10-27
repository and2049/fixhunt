const arr = Array(3);
arr[1] = 'present';
console.log(arr.length);
console.log(<div {...{ hidden: arr[1] }} />);
console.log(<div hidden={arr[0]} />);
