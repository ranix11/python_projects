import os

# --------------------------------------------------
# FOLDER TO SCAN
# --------------------------------------------------

folder_path = r"D:\Files_from_C_Drive"


# --------------------------------------------------
# FIND ALL FILES
# --------------------------------------------------

files_with_size = []

for root, folders, files in os.walk(folder_path):

    for file in files:

        file_path = os.path.join(root, file)

        try:
            file_size = os.path.getsize(file_path)

            files_with_size.append(
                (file_size, file_path)
            )

        except OSError:
            pass


# --------------------------------------------------
# SORT BY FILE SIZE - LARGEST FIRST
# --------------------------------------------------

files_with_size.sort(
    reverse=True
)


# --------------------------------------------------
# DISPLAY TOP 10
# --------------------------------------------------

print("=" * 80)
print("TOP 10 LARGEST FILES")
print("=" * 80)

for rank, (file_size, file_path) in enumerate(
    files_with_size[:10],
    start=1
):

    # Convert bytes to GB
    size_gb = file_size / (1024 ** 3)

    # Convert bytes to MB
    size_mb = file_size / (1024 ** 2)

    print(f"\n{rank}. {os.path.basename(file_path)}")
    print(f"   Size     : {size_gb:.2f} GB ({size_mb:.2f} MB)")
    print(f"   Location : {file_path}")


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

print("Total files scanned :", len(files_with_size))
print("Top files displayed :", min(10, len(files_with_size)))