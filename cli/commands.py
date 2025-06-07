from controller.remove_background_controller import RemoveBackgroundController


def remove_background(dir_image: str):
    try:
        service = RemoveBackgroundController(dir_image)
        service.execute()
    except Exception as e:
        print(f"Error: {e}")
        return
