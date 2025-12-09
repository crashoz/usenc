from .encoder import Encoder
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

    params = {k: v for k, v in HexEncoder.params.items() if k not in set(['prefix'])}
    tests = {
        'base': {
            'params': '',
            'roundtrip': True
        }
    }

    @classmethod
    def encode(cls, text: bytes, **kwargs) -> bytes:
        return HexEncoder.encode(text, prefix="%", **kwargs)

    @classmethod
    def decode(cls, text: bytes, **kwargs) -> bytes:
        return HexEncoder.decode(text, prefix="%", **kwargs)


