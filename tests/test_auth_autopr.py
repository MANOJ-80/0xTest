"""0xAutoPR smoke tests for fix ca6b1362."""


def test_module_imports_ca6b1362():
    __import__("src.auth")


def test_fix_present_ca6b1362():
    mod = __import__("src.auth", fromlist=["*"])
    assert mod is not None
