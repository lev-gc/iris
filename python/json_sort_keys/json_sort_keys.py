"""
Demonstrates that Python's json.dump sort_keys parameter supports recursion.

Python's built-in json.dump(sort_keys=True) recursively sorts keys at every
level of nested dictionaries. This module provides examples and a utility
function for use cases where custom recursive sorting behavior is needed.
"""

import json


def dumps_sorted(obj, **kwargs):
    """Serialize obj to a JSON-formatted string with keys sorted recursively.

    This is a convenience wrapper around json.dumps with sort_keys=True,
    demonstrating that the sort_keys option is applied recursively to all
    nested dictionaries.

    Args:
        obj: The Python object to serialize.
        **kwargs: Additional keyword arguments passed to json.dumps.
                  Note: sort_keys will always be set to True.

    Returns:
        str: A JSON-formatted string with all dictionary keys sorted.
    """
    kwargs["sort_keys"] = True
    return json.dumps(obj, **kwargs)


def sort_keys_recursive(obj):
    """Return a copy of obj with all dictionary keys sorted recursively.

    This function recursively sorts dictionary keys at every nesting level,
    including dictionaries inside lists. Useful for normalising data before
    comparison or storage.

    Args:
        obj: A Python object (dict, list, or primitive value).

    Returns:
        The same object with all nested dict keys sorted.
    """
    if isinstance(obj, dict):
        return {k: sort_keys_recursive(v) for k, v in sorted(obj.items())}
    if isinstance(obj, list):
        return [sort_keys_recursive(item) for item in obj]
    return obj
