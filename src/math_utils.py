def divide(a, b):
    # This will crash if b is 0
    if b == 0:

        raise ValueError("Division by zero is not allowed")

    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def get_user_data(user_id):
    # Bad dict lookup
    data = {"1": "Alice", "2": "Bob"}
    return data.get(user_id)

