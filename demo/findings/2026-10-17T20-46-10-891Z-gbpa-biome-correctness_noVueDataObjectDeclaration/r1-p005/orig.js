let count = 0;
export default {
  data: {
    get value() {
      count++;
      return count;
    }
  }
};
