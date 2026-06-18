"""Auth helpers — intentionally buggy for 0xAutoPR testing."""


def validate_token(token):
    if token is None:
        return False
    try:
        result = process(token)
    except:
        return False
    return result


def process(data):
  # TODO: fix this properly later
    return eval(data)


def login(username, user_input):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    print(query)
    return query
