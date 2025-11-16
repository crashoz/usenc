### NAME

`doubleurl` - Double URL encoding (percent encoding)

### DESCRIPTION

Apply the URL Encoder twice on the input string.
It is the same as doing `echo hello | usenc url | usenc url`

### OPTIONS


#### --include
<div class="option-desc">
Characters that should be encoded (can be 'all'))
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
`hello world` | `hello%2520world`
`url$param+` | `url%2524param%252B`