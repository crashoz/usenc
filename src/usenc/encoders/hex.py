from .encoder import EncodeError, DecodeError
from .escape import EscapeEncoder
from ..utils import escape_for_char_class, transform_keywords
import re
import pytest

class HexEncoder(EscapeEncoder):
    """
    Hexadecimal string encoding

    Encodes each character with its hex representation and an optional prefix

    Examples:
    hello world -> 68656C6C6F20776F726C64
    url$param+ -> 75726C253234706172616D253242
    """

    @classmethod
    def encode_char(cls, c: str, lowercase: bool = False, prefix: str = '', suffix: str = '', input_charset: str = 'utf8', output_charset: str = 'utf8'):
        hex_format = '{:02x}' if lowercase else '{:02X}'
        return ''.join([prefix + hex_format.format(b) + suffix for b in c.encode(output_charset)])

    @classmethod
    def decode_char(cls, seq: str, prefix: str = '', suffix: str = '', input_charset: str = 'utf8', output_charset: str = 'utf8'):
        plen = len(prefix)
        slen = len(suffix)
        hex_str = ''.join([seq[i:i+2] for i in range(plen, len(seq), slen + 2 + plen)])
        return bytes.fromhex(hex_str).decode(input_charset)