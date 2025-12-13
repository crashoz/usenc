from .encoder import Encoder
from .hex import HexEncoder

class UrlEncoder(HexEncoder):
    """
    Standard URL encoding (percent encoding)

    Encodes special characters and utf8 characters with a percent 
    prefixed hex value. Produces the same encoding as 
    javascript `encodeURIComponent` by default.

    Examples:
    hello world -> hello%20world
    url$param+ -> url%24param%2B
    """

    prefix = '%'

    # Exclude prefix parameter since it's defined as a class attribute
    params = {k: v for k, v in HexEncoder.params.items() if k not in set(['prefix'])}

    tests = {
        'base': {
            'params': '',
            'roundtrip': True
        }
    }
