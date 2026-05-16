
def separator_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n========================================\n")
        result = func(*args, **kwargs)
        print("\n========================================\n")
        return result
    return wrapper
