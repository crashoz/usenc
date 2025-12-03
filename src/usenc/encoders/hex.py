from .base import Encoder, EncodeError, DecodeError
from ..utils import escape_for_char_class, transform_keywords
import re
import pytest

class HexEncoder(Encoder):
    """
    Hexadecimal string encoding

    Encodes each character with its hex representation

    Examples:
    hello world -> 68656C6C6F20776F726C64
    url$param+ -> 75726C253234706172616D253242
    """

    params = {
        'prefix': {
            'type': str,
            'default': '',
            'help': 'Prefix string to each encoded character'
        },
        'include': {
            'type': str,
            'default': '',
            'help': 'Characters that should be encoded (can contain \'all\', \'utf8\' or \'ascii\')'
        },
        'exclude': {
            'type': str,
            'default': '',
            'help': 'Characters that should not be encoded'
        },
        'regex': {
            'type': str,
            'default': '',
            'help': 'Regex override for characters that should be encoded'
        },
        'lowercase': {
            'action': 'store_true',
            'help': 'Use lowercase hex digits'
        }
    }

    tests = {
        'base': {
            'params': '',
            'roundtrip': False
        },
        'prefix': {
            'params': '--prefix 0x',
            'roundtrip': True
        },
        'include': {
            'params': '--prefix 0x --include ghij',
            'roundtrip': True
        },
        'exclude': {
            'params': '--exclude abcd',
            'roundtrip': False
        },
        'include_all': {
            'params': '--include all',
            'roundtrip': True
        },
        'include_all_except_one': {
            'params': '--include all --exclude g',
            'roundtrip': False
        },
        'regex': {
            'params': '--regex [a-z]+',
            'roundtrip': False
        },
        'lowercase': {
            'params': '--lowercase',
            'roundtrip': False
        }
    }

    default_character_class = '^A-Za-z0-9\\-_.!~*\'()'

    @classmethod
    def encode(cls, text: bytes, prefix: str = '', include: str = '', exclude: str = '', regex: str = '', lowercase: bool = False, input_charset: str = 'utf8', output_charset: str = 'utf8', **kwargs) -> str:
        if regex == '':
            safe_include = transform_keywords(escape_for_char_class(include))
            safe_exclude = transform_keywords(escape_for_char_class(exclude))

            regex = rf'[{cls.default_character_class}]'
            if (safe_include != ''):
                regex = rf'({regex}|[{safe_include}])'
            if (safe_exclude != ''):
                regex =  rf'(?![{safe_exclude}]){regex}'
            regex = rf'(?:{regex})+'

        try:
            encRegex = re.compile(regex)
        except re.error as e:
            raise EncodeError(f'regex error: {e}') from e

        hex_format = prefix + ('{:02x}' if lowercase else '{:02X}')

        def replace(match):
            enc_string = ""
            for x in match.group(0).encode(output_charset):
                enc_string += hex_format.format(x)
            return enc_string

        try:
            return encRegex.sub(replace, text.decode(input_charset)).encode(output_charset)
        except UnicodeDecodeError as e:
            raise EncodeError(f'input-charset \'{input_charset}\' decoding failed: {e}') from e
        except UnicodeEncodeError as e:
            raise EncodeError(f'output-charset \'{output_charset}\' encoding failed: {e}') from e

    @classmethod
    def decode(cls, text: bytes, prefix: str = '', include: str = '', exclude: str = '', regex: str = '', lowercase: bool = False, input_charset: str = 'utf8', output_charset: str = 'utf8', **kwargs) -> str:
        def decode_hex_str(match):
            hex_prefixed_str = match.group(0)
            hex_str = ''.join([hex_prefixed_str[i:i+2] for i in range(len(prefix), len(hex_prefixed_str), len(prefix) + 2)])
            return bytes.fromhex(hex_str).decode(input_charset)

        try:
            return re.sub(f'({prefix}([a-fA-F0-9]{{2}}))+', decode_hex_str, text.decode(input_charset)).encode(output_charset)
        except UnicodeDecodeError as e:
            raise DecodeError(f'input-charset \'{input_charset}\' decoding failed: {e}') from e
        except UnicodeEncodeError as e:
            raise DecodeError(f'output-charset \'{output_charset}\' encoding failed: {e}') from e


def test_advanced_encode():
    with pytest.raises(EncodeError, match="regex error: unterminated character set at position 0"):
        HexEncoder.encode(b'hello world', regex='[a-z')

    with pytest.raises(EncodeError, match="input-charset 'utf8' decoding failed"):
        HexEncoder.encode(b'h\xE9llo')

    with pytest.raises(EncodeError, match="output-charset 'ascii' encoding failed"):
        HexEncoder.encode(b'h\xC3\xA9llo', output_charset='ascii')

def test_advanced_decode():
    with pytest.raises(DecodeError, match="input-charset 'utf8' decoding failed"):
        HexEncoder.decode(b'hE9llo')

    with pytest.raises(DecodeError, match="output-charset 'ascii' encoding failed"):
        HexEncoder.decode(b'h\xC3\xA9llo', output_charset='ascii')