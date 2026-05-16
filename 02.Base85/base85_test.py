"""
Unit tests for 02.Base85

"""

import base85ed


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"") == b""
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"

def test_multiple_chunks_encode():
    """
    Test longer encodes
    """
    assert base85ed.encode(b"Hello World!") == b"NM&qnZy;B1a%^NF"
    assert base85ed.encode(b"12345") == b"F)}kWH2"

def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"") == b""
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F) {") == b"12"
    assert base85ed.decode(b"F)}kW") == b"1234"

def test_multiple_chunks_decode():
    """
    Test longer decodes
    """
    assert base85ed.decode(b"F)}kWH2") == b"12345"
    assert base85ed.decode(b"NM&qnZy;B1a%^NF") == b"Hello World!"

def test_raw_decodes():
    """
    Test decodes with unnesessary whitespaces
    """
    assert base85ed.decode(b"NM&qnZy;B1\na%^NF") == b"Hello World!"
    assert base85ed.decode(b"NM&qnZ y;B1a %^NF  ") == b"Hello World!"

