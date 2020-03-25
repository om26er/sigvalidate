class TypeWithConstraints:
    length = 0
    data_type = None

    def __new__(cls):
        raise ValueError("Cannot be instantiated.")

    def __class_getitem__(cls, length):
        if not isinstance(length, int):
            raise ValueError("length must be int")
        cls.length = length
        return cls


class Str(TypeWithConstraints):
    data_type = str
    """
    Type hint that could use to provide length of string
    """


class Bytes(TypeWithConstraints):
    data_type = bytes
    """
    Type hint that could use to provide length of bytes
    """
