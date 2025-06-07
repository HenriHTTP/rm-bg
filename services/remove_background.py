from rembg import remove


class RemoveBackgroundService:
    def __init__(self, image_path: str, output_image_path: str):
        self.image_path = image_path
        self.output_image_path = output_image_path
        self.output_image = None

    def _remove_background(self) -> bytes:
        try:
            with open(self.image_path, "rb") as image_file:
                image_data = image_file.read()
            self.output_image = remove(image_data)
            return self.output_image
        except Exception as error:
            raise Exception(f"Erro ao remover o fundo: {error}")

    def _save_output_image(self):
        try:
            with open(self.output_image_path, "wb") as f:
                f.write(self.output_image)
            print(f"Imagem salva com sucesso: {self.output_image_path}")
        except Exception as error:
            raise Exception(f"Erro ao salvar a imagem: {error}")

    def execute(self):
        try:
            self._remove_background()
            self._save_output_image()
        except Exception as error:
            raise Exception(f"Erro ao executar o serviço: {error}")
