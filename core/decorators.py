
def separator_decorator(title: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("\n========================================")
            print(f" {title} ")
            print("========================================\n")
            result = func(*args, **kwargs)
            print("\n========================================\n")
            return result
        return wrapper
    return decorator
