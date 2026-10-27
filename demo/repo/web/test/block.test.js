import { test } from "node:test";
import assert from "node:assert/strict";
import { run } from "../src/block.js";

test("run logs both items", () => {
  const seen = [];
  run((x) => seen.push(x));
  assert.deepEqual(seen, [1, 2]);
});
