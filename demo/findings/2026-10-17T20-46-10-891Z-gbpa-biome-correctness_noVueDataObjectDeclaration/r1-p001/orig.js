let i = 0;
const inc = () => ++i;
export default {
  data: {
    a: inc(),
    b: inc()
  }
};
