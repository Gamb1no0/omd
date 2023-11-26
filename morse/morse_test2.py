"""Testing decode function in morse.py"""
from morse import decode
import pytest


@pytest.mark.parametrize(
    'test_input,expected',
    [('-.. . .- -.. .-.. .. -. .', 'DEADLINE'),
     ('... --- ...', 'SOS'),
     ('-.-. .- .-..', 'CALL')]
)

def test_decode(test_input, expected):
    """Testing function for decode"""
    assert decode(test_input) == expected