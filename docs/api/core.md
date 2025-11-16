# Core API Reference

The core module provides high-level functions for encoding and decoding.

## Functions

::: usenc.encode

::: usenc.decode

## Usage Examples

### Basic Usage

```python
from usenc import encode, decode

# Encode a string
encoded = encode("hello world", "url")
print(encoded)  # hello%20world

# Decode it back
decoded = decode(encoded, "url")
print(decoded)  # hello world
```

### With Parameters

```python
from usenc import encode

# Pass encoder-specific parameters
encoded = encode(
    "hello-world",
    "url",
    include="-"
)
print(encoded)  # hello%2Dworld
```

### Error Handling

```python
from usenc import encode

try:
    result = encode("test", "nonexistent")
except KeyError:
    print("Encoder not found")
```

## See Also

- [Available Encoders](../encoders/url.md) - List of all encoders
