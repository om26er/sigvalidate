### SigValidate: Signature Validation using Type Hinting

This library makes use of Python's type hinting by validating the signature of your functions.
The aim is to reduce boilerplate code as much as possible.

#### Show me some code
A basic function that must be called with a string of exactly 10 characters would look like
```python
from sigvalidate.validator import type_check
from sigvalidate.types import Str


@type_check
def test(name: Str[10]):
    print(name)
```

#### TBD