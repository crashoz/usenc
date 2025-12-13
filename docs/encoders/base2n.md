### NAME

`base2n` - Base encoder for power-of-two base encodings (base64, base32, base16, etc.)

### DESCRIPTION

This encoder works directly on bytes and returns bytes using bitwise operations.
It supports various power-of-two bases where each encoded character represents
a fixed number of bits (2, 3, 4, 5, 6, etc.).
The encoder uses a custom alphabet and handles padding appropriately.

### OPTIONS


#### --padding
<div class="option-desc">
Include padding characters (=) in output
</div>

#### --alphabet
<div class="option-desc">
Custom alphabet to use for encoding (must have correct length for the base)
</div>
