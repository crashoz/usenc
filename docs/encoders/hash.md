### NAME

`hash` - Base hash encoder using hashlib

### DESCRIPTION

This encoder computes cryptographic hashes of input bytes and outputs
the hex digest as bytes. Hash functions are one-way operations and
cannot be decoded.
Can be used directly with --hash-name parameter. Supports any hash in
your OpenSSL installation (openssl list -digest-algorithms)

### OPTIONS


#### --hash-name
<div class="option-desc">
Hash algorithm name (e.g., md5, sha256, sha512)
</div>

#### --lowercase
<div class="option-desc">
Output hex digest in lowercase
</div>
