import os


class System:
    def __init__(self):
        self.os = os

    def get_directory(self) -> str:
        return self.os.getcwd()

    def clear_screen(self) -> None:
        self.os.system("cls" if os.name == "nt" else "clear")

    def get_file_size(self, file_path: str) -> int:
        return self.os.path.getsize(file_path)

    def list_files(self, directory: str) -> list[str]:
        return self.os.listdir(directory)
