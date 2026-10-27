import sys
import os
from pathlib import Path


class Shouter(object):
    def __init__(self, suffix):
        self.suffix = suffix

    def shout(self, words):
        return [f"{w.upper()}" + self.suffix for w in words]


def present(d, wanted):
    return [k for k in d if k in wanted]


def shout(words):
    marker = f"!"
    return Shouter(marker).shout(words)


def read_first(path):
    with open(path, "r") as f:
        return f.readline().rstrip("\n")


def home():
    return str(Path(os.environ.get("HOME", "/")))


def platform():
    return sys.platform
