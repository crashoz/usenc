"""
Check the base encoder
"""

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from usenc.encoders.base import Encoder, EncodeError, DecodeError


class TestEncodeError:
    """Tests for the EncodeError exception class"""

    def test_encode_error_message(self):
        """Test that EncodeError generates correct message"""
        error = EncodeError("base64", "test string")
        assert str(error) == "Failed to encode using 'base64': 'test string'"

    def test_encode_error_attributes(self):
        """Test that EncodeError stores encoder_name and string"""
        error = EncodeError("hex", "data")
        assert error.encoder_name == "hex"
        assert error.string == "data"

class TestDecodeError:
    """Tests for the DecodeError exception class"""

    def test_decode_error_message(self):
        """Test that DecodeError generates correct message"""
        error = DecodeError("base64", "invalid data")
        assert str(error) == "Failed to decode using 'base64': 'invalid data'"

    def test_decode_error_attributes(self):
        """Test that DecodeError stores encoder_name and string"""
        error = DecodeError("hex", "xyz")
        assert error.encoder_name == "hex"
        assert error.string == "xyz"

class TestBaseEncoder:
    """Tests for the Base encoder class"""

    def test_encode_not_implemented(self):
        """Test that base Encoder.encode raises NotImplementedError"""
        with pytest.raises(NotImplementedError):
            Encoder.encode("hello, world!")

    def test_decode_not_implemented(self):
        """Test that base Encoder.decode raises NotImplementedError"""
        with pytest.raises(NotImplementedError):
            Encoder.decode("hello, world!")
