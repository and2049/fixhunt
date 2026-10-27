let count = 0;
const obj = {
  get value() {
    count++;
    return "val";
  }
};
console.log(`Start${  obj.value  }End`);
console.log(`Getter called ${  count  } times`);
