import os
import shutil

folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Python": [".py"],
    "ZIP Files": [".zip", ".rar"]
}

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        destination = "Others"

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination = folder_name
                break

        destination_path = os.path.join(folder, destination)

        os.makedirs(destination_path, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination_path, file)
        )

print("✅ Files organized successfully!")