import { test } from "node:test";
import assert from "node:assert/strict";
import { pick } from "../src/negate.js";

test("pick", () => {
  assert.equal(pick(true, "a", "b"), "b");
  assert.equal(pick(false, "a", "b"), "a");
});
