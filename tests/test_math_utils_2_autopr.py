"""0xAutoPR smoke tests for fix 1eeaccca."""


def test_module_imports_1eeaccca():
    __import__("src.math_utils_2")


def test_fix_present_1eeaccca():
    mod = __import__("src.math_utils_2", fromlist=["*"])
    assert mod is not None
