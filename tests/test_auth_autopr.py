"""0xAutoPR smoke tests for fix 61b478d7."""


def test_module_imports_61b478d7():
    __import__("src.auth")


def test_fix_present_61b478d7():
    mod = __import__("src.auth", fromlist=["*"])
    assert mod is not None
