from .base import Encoder
from .hex import HexEncoder

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
            'help': 'Characters that should be encoded (can contain \'all\' or \'utf8\')'
        },
        'exclude': {
            'type': str,
            'default': '',
            'help': 'Characters that should not be encoded'
        },
        'regex': {
            'type': str,
            'default': '',
            'help': 'Regex that matches characters that should be encoded'
        },
        'lowercase': {
            'action': 'store_true',
            'help': 'Use lowercase hex digits in percent encoding'
        }
    }

    tests = {
        'base': {
            'params': '',
            'roundtrip': True
        },
        'include': {
            'params': '--include abcd',
            'roundtrip': True
        },
        'exclude': {
            'params': '--exclude abcd',
            'roundtrip': True
        },
        'include_all': {
            'params': '--include all',
            'roundtrip': True
        },
        'include_all_except_one': {
            'params': '--include all --exclude g',
            'roundtrip': True
        },
        'regex': {
            'params': '--regex "a-z"',
            'roundtrip': False
        },
        'lowercase': {
            'params': '--lowercase',
            'roundtrip': True
        }       
    }

    @classmethod
    def encode(cls, text: str, **kwargs) -> str:
        return HexEncoder.encode(text, prefix="%", **kwargs)

    @classmethod
    def decode(cls, text: str, **kwargs) -> str:
        return HexEncoder.decode(text, prefix="%", **kwargs)


