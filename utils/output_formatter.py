from typing import List, Union

class OutputFormatter:
    # ANSI Color Codes
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    @staticmethod
    def header(text: str) -> None:
        """Print a styled header."""
        width = 50
        print(f"\n{OutputFormatter.CYAN}{OutputFormatter.BOLD}╔{'═' * (width-2)}╗")
        print(f"║{text.center(width-2)}║")
        print(f"╚{'═' * (width-2)}╝{OutputFormatter.RESET}\n")

    @staticmethod
    def section(text: str, value: str = "") -> None:
        """Print a section title with optional inline value."""
        if value:
            # Calculate padding to align values
            padding = " " * max(0, (20 - len(text)))
            print(f"{OutputFormatter.YELLOW}{OutputFormatter.BOLD}• {text}:{padding} "
                  f"{OutputFormatter.GREEN}{value}{OutputFormatter.RESET}")
        else:
            print(f"{OutputFormatter.YELLOW}{OutputFormatter.BOLD}• {text}{OutputFormatter.RESET}")

    @staticmethod
    def info(label: str, value: str) -> None:
        """Print labeled information."""
        padding = " " * max(0, (20 - len(label)))
        print(f"  {OutputFormatter.WHITE}{label}:{padding}{OutputFormatter.CYAN}{value}{OutputFormatter.RESET}")

    @staticmethod
    def solution(text: str) -> None:
        """Print a solution with highlighting."""
        print(f"  {OutputFormatter.MAGENTA}{OutputFormatter.BOLD}{text}{OutputFormatter.RESET}")

    @staticmethod
    def error(text: str) -> None:
        """Print an error message."""
        print(f"{OutputFormatter.RED}{OutputFormatter.BOLD}Error: {text}{OutputFormatter.RESET}") 