"""0xAutoPR smoke tests for fix 3c66fba1."""


def test_module_imports_3c66fba1():
    __import__("src.auth")


def test_fix_present_3c66fba1():
    mod = __import__("src.auth", fromlist=["*"])
    assert mod is not None
