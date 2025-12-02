"""
Check the base encoder
"""

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from usenc.encoders.base import Encoder, EncodeError, DecodeError

class TestBaseEncoder:
    """Tests for the Base encoder class"""

    def test_encode_not_implemented(self):
        """Test that base Encoder.encode raises NotImplementedError"""
        with pytest.raises(NotImplementedError):
            Encoder.encode(b"hello, world!")

    def test_decode_not_implemented(self):
        """Test that base Encoder.decode raises NotImplementedError"""
        with pytest.raises(NotImplementedError):
            Encoder.decode(b"hello, world!")
