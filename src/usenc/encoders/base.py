class EncodeError(Exception):
    """Exception raised when encoding fails."""
    
    def __init__(self, encoder_name: str, string: str):
        self.encoder_name = encoder_name
        self.string = string
        message = f"Failed to encode using '{encoder_name}': {string!r}"
        super().__init__(message)


class DecodeError(Exception):
    """Exception raised when decoding fails."""
    
    def __init__(self, encoder_name: str, string: str):
        self.encoder_name = encoder_name
        self.string = string
        message = f"Failed to decode using '{encoder_name}': {string!r}"
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