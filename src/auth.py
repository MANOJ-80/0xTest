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
  # TODO: fix this properly later
    return data


def login(username, user_input):
    query = "SELECT * FROM users WHERE name = ?"
    params = (username,)
    print(query)
    return query
