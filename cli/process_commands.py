from .commands  import remove_background

def process_commands(command):
    match command:
        case "help":
            print("Available commands:")
            print("help     - Show this help message")
            print("exit     - Exit the program")
            print("rmb      - Remove the background from an image")
        case "exit":
            return False
        case "rmb":
            dir_path = input("image path: ").strip().strip('"').strip("'")
            remove_background(dir_path)
        case _:
            print("Invalid command. Type 'help' to see the list of available commands.")
    return True
