"""0xAutoPR smoke tests for fix bffc658c."""


def test_module_imports_bffc658c():
    __import__("src.math_utils_3")


def test_fix_present_bffc658c():
    mod = __import__("src.math_utils_3", fromlist=["*"])
    assert mod is not None
