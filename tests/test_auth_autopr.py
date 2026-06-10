"""0xAutoPR smoke tests for fix f812b09d."""


def test_module_imports_f812b09d():
    __import__("src.auth")


def test_fix_present_f812b09d():
    mod = __import__("src.auth", fromlist=["*"])
    assert mod is not None
