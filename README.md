# SmartOrganize

SmartOrganize is a Python application that automatically organizes files into categorized folders based on their file extensions.

## Features

- Automatically organizes files by extension
- Creates destination folders when needed
- Supports multiple file formats
- Uses `pathlib` for modern file handling
- Uses `shutil` for safely moving files
- Places unsupported file types into an `Outros` folder

## Supported Categories

| Category | Extensions |
|----------|------------|
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.rtf` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv` |
| Presentations | `.ppt`, `.pptx` |
| Music | `.mp3`, `.wav`, `.flac` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Archives | `.zip`, `.rar`, `.7z` |
| Others | Any unsupported extension |

## Technologies

- Python 3
- pathlib
- shutil

## Project Structure

```text
SmartOrganize/
│
├── main.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/PedrReis-create/SmartOrganize.git
```

Go to the project folder:

```bash
cd SmartOrganize
```

Run the application:

```bash
python main.py
```

## Example

Before:

```text
Downloads/
│
├── photo.jpg
├── notes.pdf
├── music.mp3
├── video.mp4
└── report.docx
```

After:

```text
Downloads/
│
├── Imagens/
│   └── photo.jpg
├── Documentos/
│   ├── notes.pdf
│   └── report.docx
├── Musicas/
│   └── music.mp3
├── Videos/
│   └── video.mp4
└── Outros/
```

## Future Improvements

- Graphical interface (CustomTkinter)
- Drag and drop support
- Progress bar
- Undo last organization
- Duplicate file detection
- External configuration with `config.json`
- Organization summary report

## License

This project is licensed under the MIT License.