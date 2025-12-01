class EncodeError(Exception):
    """Exception raised when encoding fails."""
    
    def __init__(self, string: str):
        self.string = string
        message = f"Failed to encode: {string!r}"
        super().__init__(message)


class DecodeError(Exception):
    """Exception raised when decoding fails."""
    
    def __init__(self, string: str):
        self.string = string
        message = f"Failed to decode: {string!r}"
        super().__init__(message)

class Encoder:
    """Base class for encoders - makes adding new encoders simple"""

    params = {}
    tests = {
        'base': ''
    }
    
    @staticmethod
    def encode(text: str, **kwargs) -> str:
        raise NotImplementedError

    @staticmethod
    def decode(text: str, **kwargs) -> str:
        raise NotImplementedError