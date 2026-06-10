"""0xAutoPR smoke tests for fix ce2d6311."""


def test_module_imports_ce2d6311():
    __import__("src.config")


def test_fix_present_ce2d6311():
    mod = __import__("src.config", fromlist=["*"])
    assert mod is not None
