### NAME

`base16` - Standard Base16 encoding (RFC 4648), also known as hexadecimal encoding

### DESCRIPTION

Encodes binary data using 16 ASCII characters (0-9, A-F)
Each character represents 4 bits of data.
Alternative alphabets:
- upper: 0-9, A-F (default, uppercase)
- lower: 0-9, a-f (lowercase)

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
`hello` | `68656C6C6F`
`hello world` | `68656C6C6F20776F726C64`