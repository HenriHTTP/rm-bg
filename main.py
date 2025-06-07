from rich.text import Text
from utils.ansii.ansii_art import AnsiiArt
from rich.console import Console
from utils.system import System
from cli.process_commands import process_commands


def main():
    header = AnsiiArt()
    console = Console()
    logo = Text(header.logo, style="bold white")
    system = System()
    system.clear_screen()
    while True:
          system.clear_screen()
          console.print(logo)
          command = input(">>> ").strip()
          if not process_commands(command):
              break
          input("\nPress enter to continue.")

if __name__ == "__main__":
    main()
