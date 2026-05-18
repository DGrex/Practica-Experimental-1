import os
import shutil


class ConsoleUtils:
    @staticmethod
    def clear_screen():
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def gotoxy(x, y):
        """Move cursor to position (x, y). 1-based."""
        print(f"\033[{y};{x}H", end="")

    @staticmethod
    def print_header(text):
        """Print a header with color."""
        print(f"\n{text}\n")

    @staticmethod
    def get_console_size():
        """Get console width and height."""
        return shutil.get_terminal_size((80, 24))

    @staticmethod
    def center_text(text, width=None):
        """Center text within a given width."""
        if width is None:
            width = ConsoleUtils.get_console_size().columns
        return text.center(width)

    @staticmethod
    def print_box(title, lines, symbol="═"):
        """Print a centered box with title and content lines."""
        console_width = ConsoleUtils.get_console_size().columns
        box_width = min(console_width - 4, 120)

        # Top border
        print(f"╔{symbol * (box_width - 2)}╗".center(console_width))

        # Title
        if title:
            title_line = f"║ {title.center(box_width - 4)} ║"
            print(title_line.center(console_width))
            print(f"╠{symbol * (box_width - 2)}╣".center(console_width))

        # Content lines
        for line in lines:
            if line == "":
                print(f"║{' ' * (box_width - 2)}║".center(console_width))
            else:
                # Handle long lines by wrapping them
                if len(line) > box_width - 4:
                    # Split long lines
                    words = line.split()
                    current_line = ""
                    for word in words:
                        if len(current_line) + len(word) + 1 <= box_width - 4:
                            current_line += word + " "
                        else:
                            if current_line:
                                padding = box_width - len(current_line) - 4
                                padded_line = f"║ {current_line}{' ' * padding} ║"
                                print(padded_line.center(console_width))
                            current_line = word + " "
                    if current_line:
                        padding = box_width - len(current_line) - 4
                        padded_line = f"║ {current_line}{' ' * padding} ║"
                        print(padded_line.center(console_width))
                else:
                    padding = box_width - len(line) - 4
                    padded_line = f"║ {line}{' ' * padding} ║"
                    print(padded_line.center(console_width))

        # Bottom border
        print(f"╚{symbol * (box_width - 2)}╝".center(console_width))
