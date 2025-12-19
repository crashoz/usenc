"""usenc - String encoding utilities."""

__version__ = "0.1.0"

# public API
from .core import EncoderNotFoundError, decode, encode
from .encoders.encoder import DecodeError, EncodeError

__all__ = ["encode", "decode", "EncodeError", "DecodeError", "EncoderNotFoundError"]
