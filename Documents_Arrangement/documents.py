
import os
import shutil

# --------------------------------------------------
# SOURCE AND DESTINATION
# --------------------------------------------------

source = r"C:\Users\Acer\Downloads"
destination = r"D:\Files_from_C_Drive"


# --------------------------------------------------
# DEFINE EXTENSION GROUPS
# --------------------------------------------------

groups = {
    "Documents": {
        ".doc", ".docx", ".odt", ".txt", ".md"
    },

    "PDF": {
        ".pdf"
    },

    "Data - Spreadsheets": {
        ".csv", ".xls", ".xlsx", ".parquet", ".dbc", ".pds"
    },

    "Images": {
        ".jpg", ".jpeg", ".jgeg", ".jpag",
        ".png", ".gif", ".webp", ".avif"
    },

    "Video": {
        ".mp4", ".avi"
    },

    "Audio": {
        ".mp3"
    },

    "Code - Programming": {
        ".py", ".cpp", ".sql",
        ".html", ".htm", ".json",
        ".ipynb"
    },

    "Power BI": {
        ".pbix", ".pbids"
    },

    "Executables - Installers": {
        ".exe", ".msi", ".apk"
    },

    "Archives - Compressed": {
        ".zip", ".gz"
    },

    "System - Configuration": {
        ".ini", ".ds_store", ".bak", ".bin", ".enc"
    },

    "Development Tools": {
        ".chromedriver", ".so", ".vsix"
    },

    "Calendar": {
        ".ics"
    }
}


# --------------------------------------------------
# CREATE DESTINATION FOLDERS
# --------------------------------------------------

for group in groups:
    os.makedirs(os.path.join(destination, group), exist_ok=True)

# Folder for extensions that don't belong to a group
other_folder = os.path.join(destination, "Other - Unclassified")
os.makedirs(other_folder, exist_ok=True)


# --------------------------------------------------
# CREATE EXTENSION -> GROUP LOOKUP
# --------------------------------------------------

extension_to_group = {}

for group, extensions in groups.items():

    for extension in extensions:
        extension_to_group[extension] = group


# --------------------------------------------------
# COPY FILES
# --------------------------------------------------

total_files = 0
copied_files = 0
failed_files = 0

for root, folders, files in os.walk(source):

    for file in files:

        total_files += 1

        # Get file extension
        extension = os.path.splitext(file)[1].lower()

        # Determine destination group
        group = extension_to_group.get(
            extension,
            "Other - Unclassified"
        )

        # Destination folder
        destination_folder = os.path.join(
            destination,
            group
        )

        # Full source path
        source_file = os.path.join(root, file)

        # Full destination path
        destination_file = os.path.join(
            destination_folder,
            file
        )

        try:

            # Handle duplicate filenames
            if os.path.exists(destination_file):

                name, ext = os.path.splitext(file)

                counter = 1

                while os.path.exists(destination_file):

                    new_name = f"{name}_{counter}{ext}"

                    destination_file = os.path.join(
                        destination_folder,
                        new_name
                    )

                    counter += 1

            # Copy file
            shutil.copy2(
                source_file,
                destination_file
            )

            copied_files += 1

        except Exception as e:

            failed_files += 1

            print(
                f"Failed: {source_file}"
            )

            print(
                f"Reason: {e}"
            )


# --------------------------------------------------
# FINAL OUTPUT
# --------------------------------------------------

print("\n" + "=" * 50)
print("FILE ORGANIZATION COMPLETED")
print("=" * 50)

print("Total Files Found :", total_files)
print("Files Copied      :", copied_files)
print("Files Failed      :", failed_files)

print("\nDestination:")
print(destination)