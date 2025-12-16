from .encoder import EncodeError, DecodeError
from .escape import EscapeEncoder
from ..utils import escape_for_char_class, transform_keywords
from html.entities import name2codepoint, codepoint2name
import re
import pytest

class HtmlEncoder(EscapeEncoder):
    """
    Hexadecimal string encoding

    Encodes each character with its hex representation and an optional prefix

    Examples:
    hello world -> 68656C6C6F20776F726C64
    url$param+ -> 75726C253234706172616D253242
    """

    params = {
        **EscapeEncoder.params,
        'hex': {
            'action': 'store_true',
            'help': 'Use hexadecimal instead of decimal'
        }
    }

    tests = {
        **EscapeEncoder.tests,
        'hex': {
            'params': '--hex',
            'roundtrip': True
        }
    }

    prefix = '&#'
    suffix = ';'
    character_class: str = '<>&"\'\x80-\U0010FFFF'
    decode_class: str = '[^&#;]+'

    @classmethod
    def encode_char(cls, c: str, lowercase: bool = False, prefix: str = '', suffix: str = '', hex: bool = False, input_charset: str = 'utf8', output_charset: str = 'utf8'):
        codepoint = ord(c)
        try:
            return prefix + codepoint2name[codepoint] + suffix
        except KeyError:
            return prefix + (f'{codepoint:x}' if hex else f'{codepoint}') + suffix

    @classmethod
    def decode_char(cls, seq: str, prefix: str = '', suffix: str = '', hex: bool = False, input_charset: str = 'utf8', output_charset: str = 'utf8'):
        def replace(match):
            try:
                return chr(name2codepoint[match.group(1)])
            except KeyError:
                if hex:
                    return chr(int(match.group(1), 16))
                else:
                    return chr(int(match.group(1)))

        hex_str = re.sub(f'{prefix}(.+?){suffix}', replace, seq)
        return hex_str