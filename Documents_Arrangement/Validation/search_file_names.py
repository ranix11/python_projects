import os

# Folder where you want to search
SEARCH_LOCATION = r"D:\Files_from_C_Drive"


def search_files_and_folders(keyword):
    keyword = keyword.lower()

    file_results = []
    folder_results = []

    # Walk through all folders and subfolders
    for root, folders, files in os.walk(SEARCH_LOCATION):

        # Search folder names
        for folder in folders:
            if keyword in folder.lower():
                full_path = os.path.join(root, folder)
                folder_results.append(full_path)

        # Search file names
        for file in files:
            if keyword in file.lower():
                full_path = os.path.join(root, file)
                file_results.append(full_path)

    # Display results
    print("\n" + "=" * 70)
    print(f"SEARCH RESULTS FOR: {keyword}")
    print("=" * 70)

    print("\nFOLDERS FOUND:")
    print("-" * 70)

    if folder_results:
        for i, path in enumerate(folder_results, 1):
            print(f"{i}. {path}")
    else:
        print("No matching folders found.")

    print("\nFILES FOUND:")
    print("-" * 70)

    if file_results:
        for i, path in enumerate(file_results, 1):
            print(f"{i}. {path}")
    else:
        print("No matching files found.")

    print("\n" + "=" * 70)
    print(f"Total folders found : {len(folder_results)}")
    print(f"Total files found   : {len(file_results)}")
    print("=" * 70)


# -----------------------------
# Main program
# -----------------------------

while True:

    keyword = input("\nEnter file/folder name to search (or type 'exit'): ")

    if keyword.lower() == "exit":
        print("Search program closed.")
        break

    if not keyword.strip():
        print("Please enter a keyword.")
        continue

    search_files_and_folders(keyword)