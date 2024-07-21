"""Main Function For Problem 2 Solution"""
import argparse
import os

from generator import generate_csv_file
from processor import process_large_file, process_small_file


def main():
    """Main Entry Handler for Function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', type=str, default='output',
                        help='Output folder for generated file and parsed file')
    parser.add_argument('--records', '-r', type=int, default=1000,
                        help='Number of records to generate')
    parser.add_argument('--parallel', '-p', action='store_true',
                        help='Specify this if you want to process the file in parallel')

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    input_file = generate_csv_file(args.output, args.records)
    new_file_name = f'{input_file.split(".", maxsplit=1)[0]}_anon.csv'
    if not args.parallel:
        process_small_file(input_file, new_file_name, True)
    else:
        process_large_file(input_file, new_file_name)

if __name__ == "__main__":
    main()
