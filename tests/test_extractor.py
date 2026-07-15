import unittest
from src.extractor import ImageExtractor


class TestImageExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = ImageExtractor()

    def test_get_image_files(self):

        image_files = self.extractor.get_image_files("images")

        self.assertTrue(len(image_files) > 0)

    def test_extract_metadata(self):

        image_files = self.extractor.get_image_files("images")

        metadata = self.extractor.extract_metadata(image_files[0])

        self.assertIn("File Name", metadata)
        self.assertIn("Format", metadata)
        self.assertIn("Width", metadata)
        self.assertIn("Height", metadata)
        self.assertIn("Color Mode", metadata)
        self.assertIn("File Size (KB)", metadata)


if __name__ == "__main__":
    unittest.main()