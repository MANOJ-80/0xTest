"""Auth helpers — intentionally buggy for 0xAutoPR testing."""


def validate_token(token):
    if token == None:
        return False
    try:
        result = process(token)
    except:
        return False
    return result


def process(data):
    return eval(data)
