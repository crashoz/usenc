# Quick Start Guide

This guide will help you get started with usenc quickly.

## Basic Usage

### Command Line

The basic syntax is:

```bash
usenc <encoder> [options]
```

### Encode from stdin

```bash
echo "hello world" | usenc url
```

Output:
```
hello%20world
```

### Decode

Use the `-d` or `--decode` flag:

```bash
echo "hello%20world" | usenc url -d
```

Output:
```
hello world
```

### File Input/Output

Read from and write to files:

```bash
# Encode file
usenc url -i input.txt -o output.txt

# Decode file
usenc url -d -i encoded.txt -o decoded.txt
```

### Piping

usenc works great with Unix pipes:

```bash
# Encode and decode in a pipeline
echo "test data" | usenc url | usenc url -d

# Process multiple lines
cat file.txt | usenc url > encoded.txt
```

## Encoder-Specific Options

Each encoder may have its own options. Use `--help` after the encoder name to see them:

```bash
usenc url --help
```

For example, the `url` encoder take `--include` and `--exclude` options

```bash
echo "hello-wor.ld" | usenc url --include "-" --exclude "."
# hello%2Dwor.ld
```

## Python API

### Basic Encoding

```python
from usenc import encode, decode

# Encode
encoded = encode('hello world', 'url')
print(encoded)  # hello%20world

# Decode
decoded = decode(encoded, 'url')
print(decoded)  # hello world
```

### With Parameters

```python
from usenc import encode, decode

# Include additional characters
encoded = encode('hello-world', 'url', include='-')
print(encoded)  # hello%2Dworld

# Exclude characters from encoding
encoded = encode('path/to/file', 'url', exclude='/')
print(encoded)  # path/to/file
```

## Common Use Cases

### Encoding URL Parameters

```bash
echo "name=John Doe&email=john@example.com" | usenc url
```

### Processing Log Files

```bash
cat access.log | grep "special" | usenc url > encoded.log
```

### Batch Processing

```bash
for file in *.txt; do
    usenc url -i "$file" -o "encoded_$file"
done
```

## Next Steps

- Learn about all available [Encoders](../encoders/url.md)
- Check the [API Reference](../api/core.md)
- [Add your own encoder](../development/adding-encoders.md)
