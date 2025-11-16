# Universal String Encoder

An universal string encoder CLI tool and Python library for encoding/decoding strings in various formats.

## Features

- 🚀 **Simple CLI** - Encode/decode from stdin or files
- 🔌 **Extensible** - Easy to add new encoders
- 🎯 **Flexible** - Support for custom character sets
- 📦 **Lightweight** - No heavy dependencies
- 🧪 **Well-tested** - Comprehensive test suite with snapshot testing

## Quick Example

=== "CLI"

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

=== "Python"

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

See the [Encoders](./encoders/url.md) page for detailed documentation.

## Installation

See the [Installation Guide](getting-started/installation.md) for details.

```bash
pip install usenc
```

## Development

```bash
# Install in editable mode
pip install -e ".[dev]"

# Run tests
pytest

# Build documentation
mkdocs serve
```

## License

MIT License - see LICENSE file for details.