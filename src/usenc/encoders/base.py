class EncodeError(Exception):
    """Exception raised when encoding fails."""
    pass

class DecodeError(Exception):
    """Exception raised when decoding fails."""
    pass

class Encoder:
    """Base class for encoders - makes adding new encoders simple"""

    params = {}
    tests = {
        'base': {
            'params': '',
            'roundtrip': False
        }
    }
    
    @staticmethod
    def encode(text: str, **kwargs) -> str:
        raise NotImplementedError

    @staticmethod
    def decode(text: str, **kwargs) -> str:
        raise NotImplementedError