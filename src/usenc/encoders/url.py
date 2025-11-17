from .base import Encoder
from urllib.parse import unquote

from .hex import HexEncoder

# These are the default characters in encodeURIComponent
default_include = "utf8 \"#$%&+,/:;<=>?@[\\]^`{|}"

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
        'lowercase': {
            'action': 'store_true',
            'help': 'Use lowercase hex digits in percent encoding'
        }
    }

    tests = {
        'include': '--include abcd',
        'exclude': '--exclude abcd',
        'include_all': '--include all',
        'include_all_except_one': '--include all --exclude abcd',
        'lowercase': '--lowercase'       
    }

    @staticmethod
    def encode(text: str, include: str = '',  exclude: str = '', lowercase: bool = False) -> str:
        return HexEncoder.encode(text, prefix="%", include=default_include + include, exclude=exclude, lowercase=lowercase)

    @staticmethod
    def decode(text: str, include: str = '',  exclude: str = '', lowercase: bool = False) -> str:
        return HexEncoder.decode(text, prefix="%", include=default_include + include, exclude=exclude, lowercase=lowercase)


