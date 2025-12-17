from .encoder import EncodeError, DecodeError
from .escape import EscapeEncoder
from ..utils import escape_for_char_class, transform_keywords
import re
import pytest

class UnicodeEncoder(EscapeEncoder):
    """
    Unicode escapes encoding

    Encodes each character with its unicode representation and an optional prefix/suffix.

    Examples:
    hello world -> \\u0068\\u0065\\u006C\\u006C\\u006F\\u0020\\u0077\\u006F\\u0072\\u006C\\u0064
    café -> \\u0063\\u0061\\u0066\\u00E9
    日本語 -> \\u65E5\\u672C\\u8A9E
    🚀 -> \\u1F680
    """

    prefix = '\\u'
    suffix = ''
    decode_class: str = '[a-fA-F0-9]{2,8}'

    params = {
        **EscapeEncoder.params,
        'var_length': {
            'action': 'store_true',
            'help': 'Use variable length encoding'
        },
        'long': {
            'action': 'store_true',
            'help': 'Use 8 hex digits instead of 4'
        }
    }

    tests = {
        **EscapeEncoder.tests,
        'var_length': {
            'params': '--var-length',
            'roundtrip': True
        },
        'long': {
            'params': '--long',
            'roundtrip': True
        }
    }

    @classmethod
    def encode_char(cls, c: str, lowercase: bool = False, prefix: str = '', suffix: str = '', input_charset: str = 'utf8', output_charset: str = 'utf8', var_length: bool = False, long: bool = False):
        if var_length:
            hex_format = '{:x}' if lowercase else '{:X}'
        else:
            if long:
                hex_format = '{:08x}' if lowercase else '{:08X}'
            else:
                hex_format = '{:04x}' if lowercase else '{:04X}'

        return prefix + hex_format.format(ord(c)) + suffix

    @classmethod
    def decode_char(cls, seq: str, prefix: str = '', suffix: str = '', input_charset: str = 'utf8', output_charset: str = 'utf8', var_length: bool = False, long: bool = False):
        print(seq)
        plen = len(prefix)
        slen = len(suffix)

        decode_arr = []

        i = 0
        while i < len(seq):
            i += plen

            char = ''

            if suffix != '':
                while seq[i] != suffix[0]:
                    char += seq[i]
                    i += 1
                i += slen
            else:
                while i < len(seq) and seq[i] != prefix[0]:
                    char += seq[i]
                    i += 1

            decode_arr.append(chr(int(char, 16)))

        return ''.join(decode_arr)

    @classmethod
    def _compute_affix(cls, **kwargs):
        if kwargs['prefix'] != '':
            prefix = kwargs['prefix']
        elif kwargs['var_length']:
            prefix = '\\u{'
        elif kwargs['long']:
            prefix = '\\U'
        else:
            prefix = cls.prefix

        if kwargs['suffix'] != '':
            suffix = kwargs['suffix']
        elif kwargs['var_length']:
            suffix = '}'
        else:
            suffix = cls.suffix
        
        return prefix, suffix

    @classmethod
    def encode(cls, text, **kwargs):   
        prefix, suffix = cls._compute_affix(**kwargs)
        kwargs.pop('prefix', None)
        kwargs.pop('suffix', None)
        return super(UnicodeEncoder, cls).encode(text, prefix=prefix, suffix=suffix, **kwargs)

    @classmethod
    def decode(cls, text, **kwargs):
        prefix, suffix = cls._compute_affix(**kwargs)
        kwargs.pop('prefix', None)
        kwargs.pop('suffix', None)
        return super(UnicodeEncoder, cls).decode(text, prefix=prefix, suffix=suffix, **kwargs)