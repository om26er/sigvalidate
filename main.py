import os

from sigvalidate.validator import type_check
from sigvalidate.types import Str, Bytes


@type_check
def test(name: Str[10]):
    print(name)


@type_check
def test2(name: Bytes[10]):
    print(name)


if __name__ == '__main__':
    test('Characters')
    test2(os.urandom(10))
