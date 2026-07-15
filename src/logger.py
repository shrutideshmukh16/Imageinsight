import logging
from pathlib import Path


class ProjectLogger:

    def __init__(self):

        log_folder = Path("logs")
        log_folder.mkdir(exist_ok=True)

        log_file = log_folder / "imageinsight.log"

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            filemode="w"
        )

        self.logger = logging.getLogger("ImageInsight")

    def program_started(self):
        self.logger.info("Program started.")

    def image_processed(self, filename):
        self.logger.info(f"Processed image: {filename}")

    def error(self, message):
        self.logger.error(message)

    def program_finished(self):
        self.logger.info("Program finished.")