# import os

# # --------------------------------------------------
# # SOURCE AND DESTINATION
# # --------------------------------------------------

# source = r"C:\Users\Acer\Downloads"
# destination = r"D:\Files_from_C_Drive"


# # --------------------------------------------------
# # GET ALL FILE NAMES FROM DESTINATION
# # --------------------------------------------------

# destination_files = set()

# for root, folders, files in os.walk(destination):

#     for file in files:
#         destination_files.add(file.lower())


# # --------------------------------------------------
# # FIND FILES IN SOURCE THAT EXIST IN DESTINATION
# # --------------------------------------------------

# files_to_delete = []

# for root, folders, files in os.walk(source):

#     for file in files:

#         if file.lower() in destination_files:

#             source_file = os.path.join(root, file)

#             files_to_delete.append(source_file)


# # --------------------------------------------------
# # VALIDATION OUTPUT
# # --------------------------------------------------

# print("=" * 60)
# print("DELETE VALIDATION")
# print("=" * 60)

# print("\nSource:")
# print(source)

# print("\nDestination:")
# print(destination)

# print("\nFiles that CAN be deleted:")
# print("-" * 60)

# for file in files_to_delete:
#     print(file)

# print("\n" + "=" * 60)
# print("VALIDATION SUMMARY")
# print("=" * 60)

# print("Files found in Downloads       :", sum(
#     len(files)
#     for root, folders, files in os.walk(source)
# ))

# print("Files matching Destination     :", len(files_to_delete))

# print("\nNO FILES HAVE BEEN DELETED.")




import os

# --------------------------------------------------
# SOURCE AND DESTINATION
# --------------------------------------------------

source = r"C:\Users\Acer\Downloads"
destination = r"D:\Files_from_C_Drive"


# --------------------------------------------------
# GET ALL FILE NAMES FROM DESTINATION
# --------------------------------------------------

destination_files = set()

for root, folders, files in os.walk(destination):

    for file in files:
        destination_files.add(file.lower())


# --------------------------------------------------
# FIND FILES IN SOURCE THAT EXIST IN DESTINATION
# --------------------------------------------------

files_to_delete = []

for root, folders, files in os.walk(source):

    for file in files:

        if file.lower() in destination_files:

            source_file = os.path.join(root, file)

            files_to_delete.append(source_file)


# --------------------------------------------------
# VALIDATION OUTPUT
# --------------------------------------------------

print("=" * 70)
print("DELETE VALIDATION")
print("=" * 70)

print("\nSource:")
print(source)

print("\nDestination:")
print(destination)

print("\nFiles that will be deleted:")
print("-" * 70)

for file in files_to_delete:
    print(file)


# --------------------------------------------------
# VALIDATION SUMMARY
# --------------------------------------------------

total_source_files = sum(
    len(files)
    for root, folders, files in os.walk(source)
)

print("\n" + "=" * 70)
print("VALIDATION SUMMARY")
print("=" * 70)

print("Files found in Downloads   :", total_source_files)
print("Files matching Destination :", len(files_to_delete))


# --------------------------------------------------
# NOTHING TO DELETE
# --------------------------------------------------

if not files_to_delete:

    print("\nNo matching files found.")
    print("NO FILES HAVE BEEN DELETED.")

    exit()


# --------------------------------------------------
# CONFIRM DELETION
# --------------------------------------------------

print("\n" + "=" * 70)
print("WARNING")
print("=" * 70)

print(
    f"\n{len(files_to_delete)} file(s) will be permanently deleted "
    "from Downloads."
)

confirmation = input(
    '\nType "DELETE" to continue, or anything else to cancel: '
)


# --------------------------------------------------
# DELETE FILES
# --------------------------------------------------

if confirmation == "DELETE":

    deleted_count = 0
    failed_count = 0

    print("\n" + "=" * 70)
    print("DELETING FILES")
    print("=" * 70)

    for file in files_to_delete:

        try:

            os.remove(file)

            deleted_count += 1

            print("Deleted:", file)

        except Exception as e:

            failed_count += 1

            print("FAILED:", file)
            print("Reason:", e)


    # --------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------

    print("\n" + "=" * 70)
    print("DELETION COMPLETED")
    print("=" * 70)

    print("Files identified :", len(files_to_delete))
    print("Files deleted    :", deleted_count)
    print("Files failed     :", failed_count)

else:

    print("\n" + "=" * 70)
    print("DELETION CANCELLED")
    print("=" * 70)

    print("NO FILES HAVE BEEN DELETED.")