import os
import shutil

def organize_files(source_dir, code_folder, binary_folder):
    for root, _, files in os.walk(source_dir):
        for filename in files:
            if filename.endswith('.exe'):
                dest_folder = binary_folder
            elif filename.endswith('.cs'):
                dest_folder = code_folder
            else:
                continue

            source_path = os.path.join(root, filename)
            dest_path = os.path.join(dest_folder, filename)
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(source_path, dest_path)

if __name__ == "__main__":
    source_directory = "/home/snow/Plocha/C/C#/beginner"
    code_folder_name = "code"
    binary_folder_name = "binary"

    organize_files(source_directory, code_folder_name, binary_folder_name)
