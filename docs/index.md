# Universal String Encoder

# Work in Progress - Project is not ready for use

A universal string encoder CLI tool and Python library for encoding/decoding strings in various formats.

## Features

- 🚀 **Simple CLI** - Encode/decode from stdin or files
- 🔌 **Extensible** - Easy to add new encoders
- 🎯 **Flexible** - Support for custom character sets
- 📦 **Lightweight** - No heavy dependencies
- 🧪 **Well-tested** - Comprehensive test suite with snapshot testing

## Install

usenc is available on PyPi.

Install the CLI automatically

```bash
pipx install usenc
```

Or with traditional `pip` (in a virtual env)

```bash
pip install usenc
```

## Quick Example

### CLI

```bash
# Encode a string
echo "hello world" | usenc url
# Output: hello%20world

# Decode
echo "hello%20world" | usenc url -d
# Output: hello world

# From files
usenc url -i input.txt -o output.txt
```

### Python

```python
from usenc import encode, decode

# Encode
encoded = encode('hello world', encoder='url')
print(encoded)  # hello%20world

# Decode
decoded = decode(encoded, encoder='url')
print(decoded)  # hello world
```

## Available Encoders

- **[base16](https://crashoz.github.io/usenc/encoders/base16/)** - Standard Base16 encoding (RFC 4648), also known as hexadecimal encoding
- **[base2n](https://crashoz.github.io/usenc/encoders/base2n/)** - Base encoder for power-of-two base encodings (base64, base32, base16, etc.)
- **[base32](https://crashoz.github.io/usenc/encoders/base32/)** - Standard Base32 encoding (RFC 4648)
- **[base64](https://crashoz.github.io/usenc/encoders/base64/)** - Standard Base64 encoding (RFC 4648)
- **[cstring](https://crashoz.github.io/usenc/encoders/cstring/)** - C string escaping
- **[doubleurl](https://crashoz.github.io/usenc/encoders/doubleurl/)** - Double URL encoding (percent encoding)
- **[hash](https://crashoz.github.io/usenc/encoders/hash/)** - Base hash encoder using hashlib
- **[hex](https://crashoz.github.io/usenc/encoders/hex/)** - Hexadecimal string encoding
- **[md5](https://crashoz.github.io/usenc/encoders/md5/)** - MD5 hash encoder
- **[sha1](https://crashoz.github.io/usenc/encoders/sha1/)** - SHA-1 hash encoder
- **[sha256](https://crashoz.github.io/usenc/encoders/sha256/)** - SHA-256 hash encoder
- **[url](https://crashoz.github.io/usenc/encoders/url/)** - Standard URL encoding (percent encoding)



## Development

See the [Contributing Guide](https://crashoz.github.io/usenc/development/contributing/) and [How to add an encoder](https://crashoz.github.io/usenc/development/adding-encoders/)

## License

MIT License - see LICENSE file for details.