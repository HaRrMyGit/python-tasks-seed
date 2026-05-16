"""
Base85 encoder and decoder
"""

from __future__ import annotations
import base64
from beartype import beartype

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\
!#$%&()*+-;<=>?@^_`{|}~"  
REVERSED_ALPHABET = {ch: i for i, ch in enumerate(ALPHABET)}                      

@beartype
def encode(b: bytes):
    """
    Base85 encoder
    """
    if not b:
        return b''
    result = []
    for i in range(0, len(b), 4):
        chunk = b[i : i + 4].ljust(4, b'\x00')
        num = int.from_bytes(chunk, 'big')
        encodedChunk = []
        for _ in range(5):  
            encodedChunk.append(num % 85)
            num //= 85
        encodedChunk.reverse()
        result.extend([ALPHABET[d] for d in encodedChunk[: 1 + min(4, len(b) - i)]])
    return (''.join(result)).encode('ascii')


@beartype
def decode(b: bytes):
    """
    Base85 decoder
    """
    if not b:
        return b''
    data: str = ''.join((b.decode('ascii')).split())
    result: bytearray = bytearray()
    for i in range(0, len(data), 5):
        chunkLength = min(5, len(data) - i)
        chunk = data[i : i + chunkLength] + "!" * (5 - chunkLength)
        num = 0
        for symbol in chunk:
            num = num * 85 + REVERSED_ALPHABET[symbol]
        result.extend(num.to_bytes(4, 'big')[:chunkLength - 1])
    return bytes(result)