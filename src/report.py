import csv
from pathlib import Path
from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.output_folder = Path("output")
        self.output_folder.mkdir(exist_ok=True)

    def generate_csv(self, metadata_list):

        csv_file = self.output_folder / "metadata.csv"

        valid_data = [
            item for item in metadata_list
            if "Error" not in item
        ]

        if not valid_data:
            print("No metadata available.")
            return

        with open(csv_file, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=valid_data[0].keys()
            )

            writer.writeheader()
            writer.writerows(valid_data)

        print("\nCSV report saved successfully!")
        print(f"Location: {csv_file}")

    def generate_summary(self, metadata_list):

        summary_file = self.output_folder / "summary.txt"

        total = len(metadata_list)

        success = len([
            item for item in metadata_list
            if "Error" not in item
        ])

        failed = total - success

        with open(summary_file, "w", encoding="utf-8") as file:

            file.write("IMAGEINSIGHT SUMMARY REPORT\n")
            file.write("=" * 35 + "\n\n")

            file.write(f"Generated On : {datetime.now()}\n")
            file.write(f"Total Images : {total}\n")
            file.write(f"Successful   : {success}\n")
            file.write(f"Failed       : {failed}\n")

        print("Summary report saved successfully!")
        print(f"Location: {summary_file}")