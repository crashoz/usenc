### NAME

`hex` - Hexadecimal string encoding

### DESCRIPTION

Encodes each character with its hex representation

### OPTIONS


#### --prefix
<div class="option-desc">
Prefix string to each encoded character
</div>

#### --include
<div class="option-desc">
Characters that should be encoded (can contain 'all' or 'utf8')
</div>

#### --exclude
<div class="option-desc">
Characters that should not be encoded
</div>

#### --lowercase
<div class="option-desc">
Use lowercase hex digits
</div>

### EXAMPLES

Sample  |   Encoded
--- | ---
`hello world` | `68656C6C6F20776F726C64`
`url$param+` | `75726C253234706172616D253242`