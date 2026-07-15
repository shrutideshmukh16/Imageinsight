from pathlib import Path
from PIL import Image


class ImageExtractor:

    def __init__(self):

        self.supported_extensions = [
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        ]

    def get_image_files(self, folder_path):

        folder = Path(folder_path)

        image_files = [
            file
            for file in folder.iterdir()
            if file.suffix.lower() in self.supported_extensions
        ]

        return image_files

    def extract_metadata(self, image_path):

        try:

            with Image.open(image_path) as image:

                metadata = {
                    "File Name": image_path.name,
                    "Format": image.format,
                    "Width": image.width,
                    "Height": image.height,
                    "Color Mode": image.mode,
                    "File Size (KB)": round(image_path.stat().st_size / 1024, 2)
                }

                return metadata

        except Exception as e:

            return {
                "File Name": image_path.name,
                "Error": str(e)
            }