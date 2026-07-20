from pathlib import Path
import shutil
from collections import Counter

# File categories
FOLDER_MAPPING = {
    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".tiff": "Images",
    ".heic": "Images",
    ".raw": "Images",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".tex": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",

    # Music
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".aac": "Music",
    ".ogg": "Music",
    ".m4a": "Music",
    ".wma": "Music",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".webm": "Videos",
    ".flv": "Videos",
    ".m4v": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",

    # Executables
    ".exe": "Programs",
    ".msi": "Programs",
    ".apk": "Programs",
    ".deb": "Programs",
    ".rpm": "Programs",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".cs": "Code",
    ".go": "Code",
    ".rs": "Code",
    ".php": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".yaml": "Code",
    ".yml": "Code",
    ".sql": "Code",
    ".sh": "Code",

    # Fonts
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",

    # E-books
    ".epub": "Books",
    ".mobi": "Books",
    ".azw3": "Books",
}

SEPARATOR = "-" * 10

def show_organization_report(category_counter, analyzed_files):
    print(SEPARATOR)
    print("Organization completed successfully!")

    for category, amount in category_counter.items():
        print(f"{category}: {amount}")

    print(f"Total moved: {analyzed_files}")
    print(SEPARATOR)


def show_simulation_report(analyzed_files):
    print(SEPARATOR)
    print("Simulation completed successfully!")
    print("No files were moved.")
    print(f"Total files analyzed: {analyzed_files}")
    print(SEPARATOR)

def get_yes_no_input(prompt):
    '''Get a yes/no response from user, with validation.'''
    while True:
        response = input(prompt).lower()
        if response in ['y','n']:
            return response == 'y'
        print("Invalid answer. Please enter 'Y' or 'N'.")

def confirm_organization():
    confirmation = get_yes_no_input("Would you like to organize these files now? (Y/N): ")

    if confirmation:
        print(SEPARATOR)
        print("Starting organization...")
        print(SEPARATOR)
    return confirmation
        

def organize(directory, simulation):
    print(SEPARATOR)

    category_counter = {}
    analyzed_files = 0

    for file in directory.iterdir():

        if file.is_file():

            # Get category
            category = FOLDER_MAPPING.get(file.suffix.lower(), "Others")

            # Destination folder
            destination_folder = directory / category

            # Destination file
            destination = destination_folder / file.name

            # Generate a new name if needed
            duplicate_counter = 1

            while destination.exists():
                new_name = f"{file.stem} ({duplicate_counter}){file.suffix}"
                destination = destination_folder / new_name
                duplicate_counter += 1

            # Move file
            if not simulation:
                    try:
                        destination_folder.mkdir(exist_ok=True, parents=True)

                        print(f"Moving {file.name} -> {destination}")
                        shutil.move(file, destination)
                    except PermissionError:
                        print(f'Error: permission denied moving {file.name}')
                    except Exception as e:
                        print(f'Error moving {file.name}: {e}')

            else:
                print(f"Would move {file.name} -> {destination}")

            analyzed_files += 1

            category_counter = Counter()
            category_counter[category] += 1

    if not simulation:
        show_organization_report(category_counter, analyzed_files)

    else:
        show_simulation_report(analyzed_files)

        if confirm_organization():
            organize(directory, False)


# MENU
def main():
    folder_path = input(
        "Enter the folder path (e.g. C:/Users/Name/Desktop/Folder): "
    )

    directory = Path(folder_path)

    print("1 - Organize files")
    print("2 - Simulation")

    option = input("Choose an option: ")

    if not directory.exists():
        print("The folder does not exist.")
        print("Restart the program and try again.")
        exit()

    if option == "1":
        organize(directory, False)

    elif option == "2":
        organize(directory, True)

    else:
        print("Invalid option.")
        exit()
        
if __name__ == "__main__":
    main()


# Variable flow inside organize()
#
# directory
# │
# └── C:/Users/User/Downloads
#       │
#       ├── category
#       │      │
#       │      └── "Documents"
#       │
#       ├── destination_folder
#       │      │
#       │      └── C:/Users/User/Downloads/Documents
#       │
#       └── destination
#              │
#              └── C:/Users/User/Downloads/Documents/resume.pdf