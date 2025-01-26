import os


def rename_files_in_folder(folder_path: str, prefix="file"):
    """
    Automating Renaming Files in a Folder

    Args:
        folder_path (str): Path to the folder containing the files to be renamed
        prefix (str, optional): Prefix to the renamed files. Defaults to "file".
    """
    try:
        # List all the files in the folder
        files_list = os.listdir(folder_path)

        # Filter directories and get only files using List comprehension
        files = [f for f in files_list if os.path.isfile(os.path.join(folder_path, f))]

        # Rename the Files
        for index, filename in enumerate(files, start=1):
            # Get file extension
            file_extension = os.path.splitext(filename)[1]

            # Create new file name
            new_name = f"{prefix}_{index}{file_extension}"

            # Renaming File
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_name}")

        print("Renaming Completed Successfully!")

    except Exception as e:
        print(f"Error {e}")


# Run the Program
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    prefix = input("Enter the file prefix (default is 'file'): ").strip() or "file"
    rename_files_in_folder(folder_path=folder_path, prefix=prefix)
