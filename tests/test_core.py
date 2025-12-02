"""
Check the core API
"""

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from usenc import encode, decode

text = b"<hello world>"
encoded = b"%3Chello%20world%3E"

class TestCoreAPI:
    """Basic tests for the core API"""

    def test_encode(self):
        """Verify the encode method"""
        assert encode(text, "url") == encoded

    def test_decode(self):
        """Verify the decode method"""
        assert decode(encoded, "url") == text

    def test_encode_unknown(self):
        with pytest.raises(Exception):
            encode(text, "unknown")

    def test_decode_unknown(self):
        with pytest.raises(Exception):
            decode(encoded, "unknown")

    def test_encode_params(self):
        assert encode(b"<hello world>", "url", include="o") == b"%3Chell%6F%20w%6Frld%3E"

    def test_decode_params(self):
        assert decode(b"%3Chell%6F%20w%6Frld%3E", "url", include="o") == b"<hello world>"