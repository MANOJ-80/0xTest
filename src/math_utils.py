def divide(a, b):
    # This will crash if b is 0
    return a / b

def get_user_data(user_id):
    # Bad dict lookup
    data = {"1": "Alice", "2": "Bob"}
    return data[user_id]

