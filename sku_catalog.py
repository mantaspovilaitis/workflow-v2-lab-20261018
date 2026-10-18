"""Catalog helpers built on the SKU key canonicalizer."""

import sku_key


def unique_keys(values):
    """Return sorted, distinct canonical keys from a list of values."""
    if not isinstance(values, list):
        raise ValueError("values must be a list")

    return sorted({sku_key.canonical_key(value) for value in values})
