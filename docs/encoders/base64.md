### NAME

`base64` - Standard Base64 encoding (RFC 4648)

### DESCRIPTION

Encodes binary data using 64 ASCII characters (A-Z, a-z, 0-9, +, /)
Each character represents 6 bits of data.
Alternative alphabets:
- standard: A-Z, a-z, 0-9, +, / (default)
- url: A-Z, a-z, 0-9, -, _ (URL-safe variant)

### OPTIONS


#### --padding
<div class="option-desc">
Include padding characters (=) in output
</div>

#### --alphabet
<div class="option-desc">
Custom alphabet to use for encoding (must have correct length for the base)
</div>

### EXAMPLES

Sample  |   Encoded
--- | ---
`hello` | `aGVsbG8=`
`hello world` | `aGVsbG8gd29ybGQ=`