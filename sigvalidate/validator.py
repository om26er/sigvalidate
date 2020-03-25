import inspect
from typing import Union

from sigvalidate.types import TypeWithConstraints


def validate_type_and_length(name, provided_value, provided_type, response):
    if type(provided_value) != provided_type.data_type:
        response.append("'{}' invalid type, expected={} got={}".format(
            name, provided_type.data_type.__name__, type(provided_value).__name__))
    elif len(provided_value) != provided_type.length:
        response.append("'{}' invalid length, expected={} got={}".format(
            name, provided_type.length, len(provided_value)))


def _validate(func, *args, **kwargs):
    # Converge both args and kwargs into a dictionary
    arguments = inspect.getcallargs(func, *args, **kwargs)
    response = []
    for name, kind in func.__annotations__.items():
        if name in arguments:
            if issubclass(kind, TypeWithConstraints):
                validate_type_and_length(name, arguments[name], kind, response)
            elif getattr(kind, "__origin__", None) == Union:
                if not isinstance(arguments[name], kind.__args__):
                    response.append("'{}' required={} got={}".format(
                        name, kind.__name__, type(arguments[name]).__name__))
            elif not isinstance(arguments[name], kind):
                response.append("'{}' required={} got={}".format(
                    name, kind.__name__, type(arguments[name]).__name__))
    if response:
        raise ValueError(', '.join(response))


def type_check(func):
    def _type_check(*args, **kwargs):
        _validate(func, *args, **kwargs)
        return func(*args, **kwargs)

    return _type_check


def type_check_async(func):
    async def _type_check(*args, **kwargs):
        _validate(func, *args, **kwargs)
        return await func(*args, **kwargs)

    return _type_check
