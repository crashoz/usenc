from .encoder import Encoder
from .url import UrlEncoder

class DoubleUrlEncoder(UrlEncoder):
    """
    Double URL encoding (percent encoding)
    
    Apply the URL Encoder twice on the input string. 
    It is the same as doing `echo hello | usenc url | usenc url`

    Examples:
    hello world -> hello%2520world
    url$param+ -> url%2524param%252B
    """
    
    @classmethod
    def encode(cls, text: str, **kwargs) -> bytes:
        return super().encode(super().encode(text, **kwargs), **kwargs)

    @classmethod
    def decode(cls, text: str, **kwargs) -> bytes:
        return super().decode(super().decode(text, **kwargs), **kwargs)