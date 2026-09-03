# Command Line Input

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile


def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)

            if not data:
                break

            hobj.update(data)

    return hobj.hexdigest()


def BackupFiles(Source, Destination):
    Copied_Files = []

    print("Creating backup folder...")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, Source)

            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy only new or modified files
            if (
                not os.path.exists(dest_path)
                or calculate_hash(src_path) != calculate_hash(dest_path)
            ):
                shutil.copy2(src_path, dest_path)
                Copied_Files.append(relative)

    return Copied_Files


def DataShieldStart(Source="Data"):
    Border = "-" * 50

    BackupName = "DataShieldBackup"

    print(Border)
    print("Backup process started successfully at:", time.ctime())

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup completed successfully")
    print("Files Copied :", len(files))
    print("ZIP Archive Created :", zip_file)
    print(Border)


def main():

    Border = "-" * 50

    print(Border)
    print("------ Secure Automated Data Shield ------")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":

            print("This script is used to:")
            print("1. Create automated backups")
            print("2. Backup only new and modified files")
            print("3. Generate ZIP archives automatically")
            print("4. Execute backup process periodically")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":

            print("Usage:")
            print("python data_shield.py TimeInterval SourceDirectory")
            print("")
            print("TimeInterval  : Backup interval in minutes")
            print("SourceDirectory : Directory to backup")

        else:

            print("Invalid option")
            print("Please use --h or --u")

    elif len(sys.argv) == 3:

        print("Inside project logic")
        print("Time Interval :", sys.argv[1])
        print("Source Directory :", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(
            DataShieldStart, sys.argv[2]
        )

        print(Border)
        print("Secure Automated Data Shield started successfully")
        print("Time Interval :", sys.argv[1], "minutes")
        print("Press CTRL + C to stop execution")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:

        print("Invalid number of command line arguments")
        print("Please use --h or --u for help")

    print(Border)
    print("Thank you for using Secure Automated Data Shield")
    print(Border)


if __name__ == "__main__":
    main()
