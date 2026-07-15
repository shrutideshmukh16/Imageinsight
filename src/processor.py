from concurrent.futures import ThreadPoolExecutor, as_completed


class ImageProcessor:

    def __init__(self, extractor):
        self.extractor = extractor

    def process_images(self, image_files):

        metadata_list = []

        # Process up to 4 images simultaneously
        with ThreadPoolExecutor(max_workers=4) as executor:

            future_tasks = {
                executor.submit(self.extractor.extract_metadata, image): image
                for image in image_files
            }

            for future in as_completed(future_tasks):

                try:
                    metadata = future.result()
                    metadata_list.append(metadata)

                except Exception as e:

                    metadata_list.append({
                        "Error": str(e)
                    })

        return metadata_list