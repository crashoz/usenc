from .base import Encoder
from urllib.parse import unquote

# These are the default characters in encodeURIComponent
defaultEncSet = set(" \"#$%&+,/:;<=>?@[\\]^`{|}")

class UrlEncoder(Encoder):
    """
    Standard URL encoding (percent encoding)

    Encodes special characters and utf8 characters with a percent 
    prefixed hex ascii value. Produces the same encoding as 
    javascript `encodeURIComponent` by default.

    Examples:
    hello world -> hello%20world
    url$param+ -> url%24param%2B
    """

    params = {
        'include': {
            'type': str,
            'default': '',
            'help': 'Characters that should be encoded (can be \'all\'))'
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
        'simple_include': '--include "./"',
        'simple_exclude': '--exclude "{}"',
        'include_all': '--include all',
        'include_all_except_one': '--include all --exclude a'
    }

    @staticmethod
    def encode(text: str, include: str = '',  exclude: str = '', lowercase: bool = False) -> str:
        # Custom encode (instead of urllib.parse.quote) to apply include and exclude
        encSet = (defaultEncSet | set(include)) - set(exclude)
        hex_format = '%{:02x}' if lowercase else '%{:02X}'

        encString = ""
        for c in text:
            if (c in encSet) or (include == 'all' and c not in exclude) or (not c.isascii() and c not in exclude):
                for x in c.encode('utf-8'):
                    encString += hex_format.format(x)
            else:
                encString += c
        return encString

    @staticmethod
    def decode(text: str, include: str = '',  exclude: str = '', lowercase: bool = False) -> str:
        return unquote(text)

