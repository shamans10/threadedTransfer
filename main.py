#!/usr/bin/python3
import subprocess
import shutil
import os
from concurrent import futures
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime

MAX_WORKERS = 20

def backupFolder(folder):
    subprocess.call(["rsync",
                    "-arz",
                    "{}".format(folder),
                    '.temp/'])

def main():
    # Argument parsing
    parser = ArgumentParser(
            description='Quickly backup files and folders using rsync and multiprocessing',
            formatter_class=RawTextHelpFormatter
        )
    
    parser = ArgumentParser()
    # opts

    parser.add_argument(
            '-i', '--input', type=lambda s: [str(item) for item in s.split(',')],
            help='sets the input file location. Input can be delimited with a comma to include multiple sources'
        )
    parser.add_argument(
            '-o', '--output', type=str,
            help='sets the output file location'
        )
    parser.add_argument(
            '-a', '--archive',
            action="store_true",
            help='archives output'
        )
    parser.add_argument(
            '-d', '--date',
            action="store_true",
            help='include a datetime with your output file (useful for cronjob backups'
        )

    args = parser.parse_args()

    # If temp folder doesn't exist, make one
    if not os.path.exists(".temp"):
        os.makedirs(".temp")

    # Backup folders listed in input
    tasks = args.input
    workers = min(MAX_WORKERS, len(args.input)) # Avoid creating unnecessary threads

    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(backupFolder, tasks)
    
    # Setup export
    if args.archive:
        output = ""
        if args.output:
            output += args.output
        if args.date:
            output += datetime.now().strftime('%m-%d-%Y_%H%M%S')
        
        if output == "":
            output = "backup"
        
        shutil.make_archive(output, 'zip', ".temp")

    # finish by deleting the temp folder
    shutil.rmtree('.temp', ignore_errors=True)

if __name__ == "__main__":
    main()
