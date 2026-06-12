"""0xAutoPR smoke tests for fix ee9fc5bc."""


def test_module_imports_ee9fc5bc():
    __import__("src.math_utils_3")


def test_fix_present_ee9fc5bc():
    mod = __import__("src.math_utils_3", fromlist=["*"])
    assert mod is not None
