# SKU key notes

`canonical_key(value)` accepts strings, strips surrounding whitespace, and applies Python's Unicode `casefold()`. It raises `ValueError` for non-strings and empty or whitespace-only strings.

Tested normalization, Unicode case folding, blank input, and integer and boolean rejection with local Python checks.
