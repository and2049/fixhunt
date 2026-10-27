const base = { y: 2 };
export default {
  data: {
    x: this.y + 1
  },
  mounted() {
    console.log(this.data.x);
  }
}.call(base);
