import { test } from "node:test";
import assert from "node:assert/strict";
import { describe, greet, pair } from "../src/util.js";

test("util", () => {
  assert.equal(greet("bob"), "hello, bob!");
  assert.deepEqual(pair("k", 1), { key: "k", value: 1 });
  assert.equal(describe(-1), "negative");
  assert.equal(describe(0), "non-negative");
});
