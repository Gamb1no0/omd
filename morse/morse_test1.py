import doctest
from morse import encode


def test_encode(message: str):
    """
    Testing encode function

    >>> test_encode('SOS')
    '... --- ...'
    >>> test_encode('+') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: '+'
    """

    return encode(message)


def test_encode_whitespace(message: str):
    """
    Testing encode function with normalize_whitespace flag

    >>> test_encode_whitespace('SOS')
    [('... --- ...', 3), ('... --- ...', <class 'str'>)]
    """

    encoded_message = encode(message)
    return [(encoded_message, len(message)), (encoded_message, type(encoded_message))]


if __name__ == '__main__':
    doctest.testmod()