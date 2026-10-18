def canonical_key(value):
    """Return a normalized key for a nonblank string."""
    if not isinstance(value, str):
        raise ValueError("value must be a string")

    key = value.strip()
    if not key:
        raise ValueError("value must not be empty or whitespace-only")

    return key.casefold()
