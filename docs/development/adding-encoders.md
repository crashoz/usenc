# Adding New Encoders

This guide explains how to add new encoders to usenc.

## Quick Start

Adding a new encoder is simple thanks to automatic discovery:

1. Create a new file in `src/usenc/encoders/`
2. Define an `Encoder` subclass
3. Add docstrings for automatic documentation
4. Define tests
5. Done! It's automatically registered

## Step-by-Step Example

Let's create a hex encoder:

### 1. Create the File

Create `src/usenc/encoders/hex.py`:

```python
from .base import Encoder

class Base64Encoder(Encoder):
    @staticmethod
    def encode(text: str, **kwargs) -> str:
        return base64.b64encode(text.encode('utf-8')).decode('ascii')

    @staticmethod
    def decode(text: str, **kwargs) -> str:
        return base64.b64decode(text.encode('ascii')).decode('utf-8')
```

### 2. Add custom parameters

```python
from .base import Encoder
import base64

class Base64Encoder(Encoder):

    params = {
        'separator': {
            'type': str,
            'default': '-',
            'help': 'Character to use as separator'
        },
        'uppercase': {
            'action': 'store_true',
            'help': 'Convert to uppercase'
        }
    }

    @staticmethod
    def encode(text: str, **kwargs) -> str:
        return base64.b64encode(text.encode('utf-8')).decode('ascii')

    @staticmethod
    def decode(text: str, **kwargs) -> str:
        return base64.b64decode(text.encode('ascii')).decode('utf-8')
```

## Parameter Specification

Each parameter in `params` dict should have:

- `type`: The parameter type (`str`, `bool`, `int`, etc.)
- `default`: Default value if not provided
- `help`: Help text shown in CLI



### 3. Adding Documentation

Documentation is generated from docstrings in the Encoder class:

```python
from .base import Encoder

class MyEncoder(Encoder):
    """

    """

    params = {
        'separator': {
            'type': str,
            'default': '-',
            'help': 'Character to use as separator'
        },
        'uppercase': {
            'type': bool,
            'default': False,
            'help': 'Convert to uppercase'
        }
    }

    @staticmethod
    def encode(text: str, separator: str = '-', uppercase: bool = False, **kwargs) -> str:
        result = text.replace(' ', separator)
        if uppercase:
            result = result.upper()
        return result

    @staticmethod
    def decode(text: str, separator: str = '-', uppercase: bool = False, **kwargs) -> str:
        return text.replace(separator, ' ')
```

Parameters are automatically added to the CLI:

```bash
usenc myencoder --separator "_" --uppercase
```

### 2. That's It!

The encoder is automatically discovered and registered as `base64`.

The naming convention is:
- Class name: `{Name}Encoder` → registered as `{name}`
- Example: `Base64Encoder` → `base64`


## Testing Your Encoder

### Add Test Samples

The test suite automatically tests all encoders against `tests/test_samples.txt`.

Your encoder will be tested with all samples automatically.

### Generate Snapshots

Run tests to generate snapshot files:

```bash
pytest tests/test_encodings.py
```

This creates `tests/snapshots/myencoder.txt` with expected outputs.

To re-generate snapshots, simply delete the file `tests/snapshots/myencoder.txt`.

### Manual Testing

Test from CLI:

```bash
echo "test data" | usenc myencoder
```

Test from Python:

```python
from usenc import encode

result = encode('test', 'myencoder')
print(result)
```

## Best Practices

### 1. Follow the Interface

Always implement both `encode` and `decode`:

```python
@staticmethod
def encode(text: str, **kwargs) -> str:
    pass

@staticmethod
def decode(text: str, **kwargs) -> str:
    pass
```

### 2. Handle Edge Cases

```python
@staticmethod
def encode(text: str, **kwargs) -> str:
    # Handle empty string
    if not text:
        return ''

    # Handle special characters
    # Handle encoding errors
    try:
        result = do_encoding(text)
    except Exception as e:
        # Handle gracefully
        pass

    return result
```

### 3. Add Documentation

Use docstrings:

```python
class MyEncoder(Encoder):
    """
    My encoder description

    Encodes text by doing X, Y, Z.
    Common use cases include...
    """

    @staticmethod
    def encode(text: str, param: str = '', **kwargs) -> str:
        """
        Encode text using my algorithm

        Args:
            text: The text to encode
            param: Optional parameter

        Returns:
            Encoded text
        """
        pass
```

### 4. Keep Parameters Consistent

If your encoder uses `include`/`exclude` like the URL encoder, use the same parameter names for consistency.

### 5. UTF-8 Support

Always handle UTF-8 properly:

```python
# When working with bytes
text.encode('utf-8')
bytes_data.decode('utf-8')
```

## Example: Complete Encoder

Here's a complete example with all best practices:

```python
from .base import Encoder

class HexEncoder(Encoder):
    """
    Hexadecimal encoding

    Converts each character to its hexadecimal representation.
    """

    params = {
        'uppercase': {
            'type': bool,
            'default': True,
            'help': 'Use uppercase hex digits'
        },
        'prefix': {
            'type': str,
            'default': '',
            'help': 'Prefix for each hex value (e.g., "0x")'
        }
    }

    @staticmethod
    def encode(text: str, uppercase: bool = True, prefix: str = '', **kwargs) -> str:
        """
        Encode text to hexadecimal

        Args:
            text: Text to encode
            uppercase: Use uppercase hex digits (default: True)
            prefix: Prefix for each hex value (default: '')

        Returns:
            Hexadecimal encoded string
        """
        if not text:
            return ''

        result = []
        for char in text:
            hex_val = hex(ord(char))[2:]
            if uppercase:
                hex_val = hex_val.upper()
            result.append(prefix + hex_val)

        return ' '.join(result)

    @staticmethod
    def decode(text: str, prefix: str = '', **kwargs) -> str:
        """
        Decode hexadecimal to text

        Args:
            text: Hex string to decode
            prefix: Prefix to remove from each hex value

        Returns:
            Decoded text
        """
        if not text:
            return ''

        result = []
        for hex_val in text.split():
            if prefix and hex_val.startswith(prefix):
                hex_val = hex_val[len(prefix):]
            result.append(chr(int(hex_val, 16)))

        return ''.join(result)
```

## Next Steps

- Submit a pull request
- Share your encoder with the community!
