### NAME

`cstring` - C string escaping

### DESCRIPTION

Encodes special characters and utf8 characters with a \x
prefixed hex value.

### OPTIONS


#### --include
<div class="option-desc">
Characters that should be encoded (can contain 'all', 'utf8' or 'ascii')
</div>

#### --exclude
<div class="option-desc">
Characters that should not be encoded
</div>

#### --regex
<div class="option-desc">
Regex override for characters that should be encoded
</div>

#### --lowercase
<div class="option-desc">
Use lowercase hex digits
</div>

### EXAMPLES

Sample  |   Encoded
--- | ---
`hello world` | `hello\x20world`
`url$param+` | `url\x24param\x2B`