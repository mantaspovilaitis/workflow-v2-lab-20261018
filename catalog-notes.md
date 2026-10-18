# Catalog notes

`unique_keys(values)` requires a list, passes each element to `sku_key.canonical_key`, and returns sorted unique canonical keys. It raises `ValueError` for a non-list or an element rejected by A. It does not mutate the input.

Tested normalization, ordering, Unicode case folding, empty lists, invalid container and element types, input preservation, and calls into the prerequisite function with local Python checks.
