from .base import Encoder, DecodeError
import re

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
            'default': 'all',
            'help': 'Characters that should be encoded (can contain \'all\' or \'utf8\')'
        },
        'exclude': {
            'type': str,
            'default': '',
            'help': 'Characters that should not be encoded'
        },
        'lowercase': {
            'action': 'store_true',
            'help': 'Use lowercase hex digits in percent encoding'
        }
    }

    tests = Encoder.tests | {
        'prefix': '--prefix 0x',
        'include': '--prefix 0x --include ghij',
        'exclude': '--exclude abcd',
        'include_all': '--include all',
        'include_all_except_one': '--include all --exclude ghij',
        'lowercase': '--lowercase'
    }

    @staticmethod
    def encode(text: str, prefix: str = '', include: str = '', exclude: str = '', lowercase: bool = False) -> str:
        include_utf8 = 'utf8' in include
        include = include.replace('utf8', '')
        include_all = 'all' in include
        include = include.replace('all', '')

        include_set = set(include)
        exclude_set = set(exclude)
        hex_format = prefix + ('{:02x}' if lowercase else '{:02X}')

        enc_string = ""
        for c in text:
            if c in exclude_set:
                enc_string += c
            else:
                if c in include_set or include_all or (include_utf8 and not c.isascii()):
                    for x in c.encode('utf-8'):
                        enc_string += hex_format.format(x)
                else:
                    enc_string += c

        return enc_string

    @staticmethod
    def decode(text: str, prefix: str = '', include: str = '', exclude: str = '', lowercase: bool = False) -> str:
        def decode_hex_str(match):
            hex_prefixed_str = match.group(0)
            hex_str = ''.join([hex_prefixed_str[i:i+2] for i in range(len(prefix), len(hex_prefixed_str), len(prefix) + 2)])
            return bytes.fromhex(hex_str).decode('utf-8')

        try:
            return re.sub(f'({prefix}([a-fA-F0-9]{{2}}))+', decode_hex_str, text)
        except UnicodeDecodeError:
            raise DecodeError('hex', text)
