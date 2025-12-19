### NAME

`escape` - Generic escape encoder.

### DESCRIPTION

Encodes each character with the `cls.encode_char` function and add a prefix and a suffix.
Characters to be encoded are selected by the `character_class` or `regex` parameter, and are
fine tuned by the `include` and `exclude` parameters.
The decoder uses `decode_class` to match sequences to be decoded by the `cls.decode_char` function

### OPTIONS


#### --prefix
<div class="option-desc">
Prefix string to each encoded character
</div>

#### --suffix
<div class="option-desc">
Suffix string to each encoded character
</div>

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
