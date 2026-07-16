# 🖼️ ImageInsight

A Python-based application that extracts metadata from multiple images using concurrent programming. The project processes images efficiently with **ThreadPoolExecutor**, generates reports, logs execution details, and includes unit testing.

---

## ✨ Features

- Extract image metadata
- Supports JPG, JPEG, PNG and WebP images
- Parallel image processing using ThreadPoolExecutor
- CSV report generation
- Summary report generation
- Logging support
- Regex-based filename validation
- Exception handling
- Unit testing using unittest

---

## 📁 Project Structure

```
ImageInsight
│
├── images/
├── logs/
├── output/
├── src/
│   ├── extractor.py
│   ├── processor.py
│   ├── report.py
│   ├── logger.py
│
├── tests/
│   └── test_extractor.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

- Python 3
- Pillow
- pathlib
- csv
- logging
- concurrent.futures
- re (Regex)
- unittest

---

## 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/imageinsight.git
```

Move into the project.

```bash
cd imageinsight
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🧪 Run Unit Tests

```bash
python -m unittest discover -s tests -v
```

---

## 📄 Output

The project generates:

- metadata.csv
- summary.txt
- imageinsight.log

---

## 📌 Future Improvements

- GUI using Tkinter or PyQt
- Drag & Drop image support
- PDF report generation
- Image preview
- EXIF metadata extraction
- Progress bar
- Folder selection dialog

---

## 👩‍💻 Author

Shruti Deshmukh
