from services.remove_background import RemoveBackgroundService
import os


class RemoveBackgroundController:
    def __init__(self, image_path: str):
        self.image_path = os.path.abspath(image_path)
        image_name = os.path.basename(self.image_path)
        name, ext = os.path.splitext(image_name)
        image_dir = os.path.dirname(self.image_path)
        output_image_name = f"{name}-removed{ext}"
        output_image_path = os.path.join(image_dir, output_image_name)

        self.service = RemoveBackgroundService(
            image_path=self.image_path, output_image_path=output_image_path
        )

    def execute(self):
        try:
            self.service.execute()
        except Exception as e:
            print(f"Error: {e}")
