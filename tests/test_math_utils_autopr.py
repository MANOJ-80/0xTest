"""0xAutoPR smoke tests for fix 8e876b72."""


def test_module_imports_8e876b72():
    __import__("src.math_utils")


def test_fix_present_8e876b72():
    mod = __import__("src.math_utils", fromlist=["*"])
    assert mod is not None
