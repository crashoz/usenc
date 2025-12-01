from .base import Encoder
from .url import UrlEncoder

class DoubleUrlEncoder(Encoder):
    """
    Double URL encoding (percent encoding)
    
    Apply the URL Encoder twice on the input string. 
    It is the same as doing `echo hello | usenc url | usenc url`

    Examples:
    hello world -> hello%2520world
    url$param+ -> url%2524param%252B
    """

    params = UrlEncoder.params
    tests = UrlEncoder.tests
    
    @staticmethod
    def encode(text: str, **kwargs) -> str:
        return UrlEncoder.encode(UrlEncoder.encode(text, **kwargs), **kwargs)

    @staticmethod
    def decode(text: str, **kwargs) -> str:
        return UrlEncoder.decode(UrlEncoder.decode(text, **kwargs), **kwargs)