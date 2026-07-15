import re
from src.extractor import ImageExtractor
from src.processor import ImageProcessor
from src.report import ReportGenerator
from src.logger import ProjectLogger


class ImageInsight:

    def __init__(self):
        self.image_folder = "images"
        self.extractor = ImageExtractor()
        self.processor = ImageProcessor(self.extractor)
        self.report = ReportGenerator()
        self.logger = ProjectLogger()

    def is_valid_filename(self, filename):

        pattern = r"^[A-Za-z0-9_\-\s]+\.(jpg|jpeg|png|webp)$"

        return bool(re.match(pattern, filename, re.IGNORECASE))

    def print_metadata(self, metadata):

        print("-" * 50)

        for key, value in metadata.items():
            print(f"{key:<15}: {value}")

    def run(self):

        print("\n" + "=" * 55)
        print("        IMAGEINSIGHT")
        print("   Parallel Image Metadata Extractor")
        print("=" * 55)

        self.logger.program_started()

        image_files = self.extractor.get_image_files(self.image_folder)

        if not image_files:
            print("No images found.")
            return

        print(f"\nTotal Images Found : {len(image_files)}")

        valid_images = []

        for image in image_files:

            if self.is_valid_filename(image.name):
                valid_images.append(image)
            else:
                print(f"Invalid filename : {image.name}")

        metadata_list = self.processor.process_images(valid_images)

        for metadata in metadata_list:

            self.print_metadata(metadata)

            if "Error" not in metadata:
                self.logger.image_processed(metadata["File Name"])
            else:
                self.logger.error(metadata["Error"])

        self.report.generate_csv(metadata_list)
        self.report.generate_summary(metadata_list)

        self.logger.program_finished()

        print("\nMetadata extraction completed successfully.")


if __name__ == "__main__":

    app = ImageInsight()
    app.run()