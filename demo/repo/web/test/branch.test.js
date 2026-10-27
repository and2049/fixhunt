import { test } from "node:test";
import assert from "node:assert/strict";
import { label } from "../src/branch.js";

test("label", () => {
  assert.equal(label(1), "positive");
  assert.equal(label(0), "non-positive");
});
