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