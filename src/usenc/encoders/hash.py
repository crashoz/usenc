from .encoder import Encoder, EncodeError, DecodeError
import hashlib

class HashEncoder(Encoder):
    """
    Base hash encoder using python hashlib

    This encoder computes cryptographic hashes of input bytes and outputs
    the resulting hex digest. Hash functions are one-way operations and
    cannot be decoded.

    Can be used directly with --hash-name parameter. Supports any hash in
    your OpenSSL installation (`openssl list -digest-algorithms`)

    Examples:
    hello world (md5) -> 5EB63BBBE01EEED093CB22BB8F5ACDC3
    hello world (ripemd) -> 98C615784CCB5FE5936FBC0CBE9DFDB408D92F0F
    hello world (sha3-224) -> DFB7F18C77E928BB56FAEB2DA27291BD790BC1045CDE45F3210BB6C5
    """

    params = {
        'hash_name': {
            'type': str,
            'default': None,
            'required': True,
            'help': 'Hash algorithm name (e.g., md5, sha256, sha512)'
        },
        'lowercase': {
            'action': 'store_true',
            'help': 'Output hex digest in lowercase'
        }
    }

    tests = {
        'base': {
            'params': '--hash-name sha256',
            'roundtrip': False
        },
        'lowercase': {
            'params': '--hash-name sha256 --lowercase',
            'roundtrip': False
        }
    }

    # Subclasses can define this to avoid requiring hash_name parameter
    hash_name: str = None

    @classmethod
    def encode(cls, text: bytes, hash_name: str = None, lowercase: bool = False, **kwargs) -> bytes:
        """
        Compute hash of input bytes and return hex digest as bytes

        Args:
            text: Input bytes to hash
            hash_name: Hash algorithm name (required if not defined in class)
            lowercase: If True, output lowercase hex; otherwise uppercase

        Returns:
            Hex digest as bytes
        """
        # Use parameter if provided, otherwise fall back to class attribute
        algorithm = hash_name if hash_name is not None else cls.hash_name

        if algorithm is None:
            raise EncodeError(f"hash_name parameter is required")

        try:
            hasher = hashlib.new(algorithm)
        except ValueError as e:
            raise EncodeError(f"Unknown hash algorithm '{algorithm}': {e}") from e

        hasher.update(text)
        digest = hasher.hexdigest()

        if not lowercase:
            digest = digest.upper()

        return digest.encode('ascii')

    @classmethod
    def decode(cls, text: bytes, **kwargs) -> bytes:
        """
        Hash functions are one-way and cannot be decoded

        Raises:
            DecodeError: Always, as hashes cannot be reversed
        """
        raise DecodeError(f"{cls.__name__}: hash functions cannot be decoded (one-way operation)")
