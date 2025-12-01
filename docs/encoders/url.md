### NAME

`url` - Standard URL encoding (percent encoding)

### DESCRIPTION

Encodes special characters and utf8 characters with a percent
prefixed hex ascii value. Produces the same encoding as
javascript `encodeURIComponent` by default.

### OPTIONS


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
Use lowercase hex digits in percent encoding
</div>

### EXAMPLES

Sample  |   Encoded
--- | ---
`hello world` | `hello%20world`
`url$param+` | `url%24param%2B`