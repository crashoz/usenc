from .encoder import Encoder
from .hex import HexEncoder

class CString(HexEncoder):
    """
    C string escaping

    Encodes special characters and utf8 characters with a \\x 
    prefixed hex value. 

    Examples:
    hello world -> hello\\x20world
    url$param+ -> url\\x24param\\x2B
    """

    character_class: str = '^A-Za-z0-9\\-_.!~*\'()'
    prefix = '\\x'

    # Exclude prefix parameter since it's defined as a class attribute
    params = {k: v for k, v in HexEncoder.params.items() if k not in set(['prefix'])}

    tests = {
        'base': {
            'params': '',
            'roundtrip': True
        }
    }
