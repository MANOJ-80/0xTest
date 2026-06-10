def test_validate_token_rejects_none():
    from src.auth import validate_token
    assert validate_token(None) is False
