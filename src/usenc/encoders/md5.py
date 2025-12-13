from .hash import HashEncoder


class Md5Encoder(HashEncoder):
    """
    MD5 hash encoder

    Computes MD5 hash of input bytes and outputs the hex digest as bytes.
    MD5 is a one-way hash function and cannot be decoded.

    Note: MD5 is cryptographically broken and should not be used for security purposes.

    Examples:
    hello world -> 5EB63BBBE01EEED093CB22BB8F5ACDC3
    """

    hash_name = 'md5'

    # Exclude hash_name parameter since it's defined as a class attribute
    params = {k: v for k, v in HashEncoder.params.items() if k not in set(['hash_name'])}

    tests = {
        'base': {
            'params': '',
            'roundtrip': False
        },
        'lowercase': {
            'params': '--lowercase',
            'roundtrip': False
        }
    }
