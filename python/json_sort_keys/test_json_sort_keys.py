import json
import unittest

from json_sort_keys import dumps_sorted, sort_keys_recursive


class TestJsonDumpSortKeysRecursive(unittest.TestCase):
    """Tests that verify recursive sort_keys behaviour in json.dump."""

    def test_builtin_sort_keys_is_recursive(self):
        """json.dump sort_keys=True sorts keys at every nesting level."""
        data = {"z": 1, "a": {"z": 2, "a": 3}}
        result = json.dumps(data, sort_keys=True)
        self.assertEqual(result, '{"a": {"a": 3, "z": 2}, "z": 1}')

    def test_dumps_sorted_top_level(self):
        data = {"z": 1, "m": 2, "a": 3}
        result = dumps_sorted(data)
        self.assertEqual(result, '{"a": 3, "m": 2, "z": 1}')

    def test_dumps_sorted_nested_dict(self):
        data = {"z": {"y": 1, "b": 2}, "a": {"x": 3, "c": 4}}
        result = dumps_sorted(data)
        self.assertEqual(result, '{"a": {"c": 4, "x": 3}, "z": {"b": 2, "y": 1}}')

    def test_dumps_sorted_deeply_nested(self):
        data = {"z": {"y": {"w": 1, "a": 2}, "b": 3}, "a": 4}
        result = dumps_sorted(data)
        self.assertEqual(result, '{"a": 4, "z": {"b": 3, "y": {"a": 2, "w": 1}}}')

    def test_dumps_sorted_list_of_dicts(self):
        data = [{"z": 1, "a": 2}, {"y": 3, "b": 4}]
        result = dumps_sorted(data)
        self.assertEqual(result, '[{"a": 2, "z": 1}, {"b": 4, "y": 3}]')

    def test_dumps_sorted_kwargs_forwarded(self):
        data = {"b": 1, "a": 2}
        result = dumps_sorted(data, indent=2)
        self.assertEqual(result, '{\n  "a": 2,\n  "b": 1\n}')

    def test_sort_keys_recursive_dict(self):
        data = {"z": 1, "a": 2}
        self.assertEqual(sort_keys_recursive(data), {"a": 2, "z": 1})

    def test_sort_keys_recursive_nested(self):
        data = {"z": {"y": 1, "a": 2}, "a": 3}
        result = sort_keys_recursive(data)
        self.assertEqual(list(result.keys()), ["a", "z"])
        self.assertEqual(list(result["z"].keys()), ["a", "y"])

    def test_sort_keys_recursive_list(self):
        data = [{"z": 1, "a": 2}, {"y": 3, "b": 4}]
        result = sort_keys_recursive(data)
        self.assertEqual(list(result[0].keys()), ["a", "z"])
        self.assertEqual(list(result[1].keys()), ["b", "y"])

    def test_sort_keys_recursive_mixed(self):
        data = {"z": [{"y": 1, "a": 2}], "a": {"w": 3, "b": 4}}
        result = sort_keys_recursive(data)
        self.assertEqual(list(result.keys()), ["a", "z"])
        self.assertEqual(list(result["a"].keys()), ["b", "w"])
        self.assertEqual(list(result["z"][0].keys()), ["a", "y"])

    def test_sort_keys_recursive_primitives(self):
        self.assertEqual(sort_keys_recursive(42), 42)
        self.assertEqual(sort_keys_recursive("hello"), "hello")
        self.assertEqual(sort_keys_recursive(None), None)
        self.assertEqual(sort_keys_recursive([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
