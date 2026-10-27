const ctx = { y: 5 };
export default {
  data: {
    x: this.y * 2
  },
  created() {
    console.log(this.data.x);
  }
}.call(ctx);
