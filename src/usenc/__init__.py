"""usenc - String encoding utilities."""

__version__ = "0.1.0"

# public API
from .core import encode, decode

__all__ = [
    "encode",
    "decode",
]