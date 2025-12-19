# Universal String Encoder

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
# Get help and parameters
usenc --help
usenc unicode --help
```

```bash
# Encode a string
echo "hello world" | usenc url
# Output: hello%20world

# Decode
echo "hello%20world" | usenc url -d
# Output: hello world

# File input/output
usenc url -i input.txt -o output.txt

# More complex encoding
echo "hello world" | usenc hex --prefix '${' --suffix '}' --lowercase
# Output: ${68}${65}${6c}${6c}${6f}${20}${77}${6f}${72}${6c}${64}

# Optional character selection
echo "hello world" | usenc cstring --include e
# Output: h\x65llo\x20world
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

- **[base16](https://crashoz.github.io/usenc/encoders/base16/)** - Standard Base16 encoding (RFC 4648)
- **[base32](https://crashoz.github.io/usenc/encoders/base32/)** - Standard Base32 encoding (RFC 4648)
- **[base64](https://crashoz.github.io/usenc/encoders/base64/)** - Standard Base64 encoding (RFC 4648)
- **[cstring](https://crashoz.github.io/usenc/encoders/cstring/)** - C string escaping
- **[doubleurl](https://crashoz.github.io/usenc/encoders/doubleurl/)** - Double URL encoding (RFC 3986 percent encoding)
- **[hash](https://crashoz.github.io/usenc/encoders/hash/)** - Base hash encoder using python hashlib
- **[hex](https://crashoz.github.io/usenc/encoders/hex/)** - Hexadecimal string encoding
- **[html](https://crashoz.github.io/usenc/encoders/html/)** - HTML Entities encoding
- **[md5](https://crashoz.github.io/usenc/encoders/md5/)** - MD5 hash encoding
- **[sha1](https://crashoz.github.io/usenc/encoders/sha1/)** - SHA-1 hash encoding
- **[sha256](https://crashoz.github.io/usenc/encoders/sha256/)** - SHA-256 hash encoding
- **[unicode](https://crashoz.github.io/usenc/encoders/unicode/)** - Unicode escapes encoding
- **[url](https://crashoz.github.io/usenc/encoders/url/)** - Standard URL encoding (RFC 3986 percent encoding)



## Optional Encoding

Some encoders provide the option to select which characters should be encoded (e.g. `url` or `cstring`). Those have a default setting that can be augmented with `--include some_chars` and `--exclude some_chars`. 

Advanced users can specify directly `--regex match_chars` that will override these parameters.

## Global Parameters

The bulk (`-b`or `--bulk`) parameter makes the encoder process the whole file instead of line by line. This mode can be useful for encoders like **base64** or **md5**.

For some encoders, the way the input bytes and output bytes are interpreted into strings matter. You can use parameters `--input-charset` and `--output-charset` to set the charsets used by the encoder. They both default to `utf8` which should be fine in most situations.

```bash
echo héllo | usenc url --output-charset utf8
> h%C3%A9llo
echo héllo | usenc url --output-charset latin1
> h%E9llo
echo h%E9llo | usenc url -d --input-charset latin1
> héllo
```

## Development

See the [Contributing Guide](https://crashoz.github.io/usenc/development/contributing/) and [How to add an encoder](https://crashoz.github.io/usenc/development/adding-encoders/)

## License

MIT License - see LICENSE file for details.