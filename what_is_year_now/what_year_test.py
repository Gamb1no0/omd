import urllib.request
import io
from unittest.mock import patch
import pytest
from what_is_year_now import what_is_year_now


def test_year1():
    """Test 1"""
    data = io.StringIO('{\'currentDateTime\': \'2022-11-13\'}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        assert what_is_year_now() == 2022


def test_year2():
    """Test 2"""
    data = io.StringIO('{\'currentDateTime\': \'13.11.2022\'}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        assert what_is_year_now() == 2022


def test_year3():
    """Test 3"""
    data = io.StringIO('{\'currentDateTime\': \'13-11-2022\'}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_year4():
    """Test 4"""
    data = io.StringIO('{\'DateTime\': \'13-11-2022\'}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        with pytest.raises(KeyError):
            what_is_year_now()