from core.console_utils import ConsoleUtils
import io
import sys


def separator_decorator(title: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Capture stdout
            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()

            # Execute function
            result = func(*args, **kwargs)

            # Get captured output
            sys.stdout = old_stdout
            output = captured_output.getvalue()

            # Display in a centered box
            ConsoleUtils.clear_screen()
            output_lines = output.strip().split("\n") if output.strip() else [""]
            ConsoleUtils.print_box(title, output_lines)

            return result

        return wrapper

    return decorator
