import { test } from "node:test";
import assert from "node:assert/strict";
import { parseAll } from "../src/parse.js";

test("parseAll adds the converter's value", () => {
  assert.deepEqual(parseAll(["10", "200"], (v) => v.length), [12, 203]);
});
