import sys
from file_concatenator import FileConcatenator
from utilities import uniform_file_types

import argparse
import os

import argparse
import os


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Concatenate files')
    parser.add_argument('-f', '--files', nargs='+', help='List of files to concatenate')
    parser.add_argument('-d', '--directories', nargs='+', help='List of directories to read files from')
    parser.add_argument('-o', '--output', required=True, help='Output file name')
    args = parser.parse_args()

    # Get list of input files
    input_files = []
    if args.files:
        input_files += args.files
    if args.directories:
        for directory in args.directories:
            for file in os.listdir(directory):
                input_files.append(os.path.join(directory, file))

    # Concatenate files
    if uniform_file_types(input_files) != None:
        concatenator = FileConcatenator()
    else:
        print("Error: Cannot concatenate files of different types")
        return

    concatenator.concatenate_files(input_files, args.output)
    print("Successfully concatenated files into", args.output)

if __name__ == "__main__":
    main()