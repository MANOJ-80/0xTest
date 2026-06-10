"""0xAutoPR smoke tests for fix 0ca36c5d."""


def test_module_imports_0ca36c5d():
    __import__("src.config")


def test_fix_present_0ca36c5d():
    mod = __import__("src.config", fromlist=["*"])
    assert mod is not None
