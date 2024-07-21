"""Main Function For Problem 1 Solution"""
import argparse
import csv
from random import randint
from typing import Generator
import os


SPEC = {
    'ItemName': 10,
    'Price': 3,
    'Quantity': 4,
    'Category': 7
}


DATA = [
    {
        'ItemName': 'Apple',
        'Price': '10',
        'Quantity': '5',
        'Category': 'Fruit'
    },
    {
        'ItemName': 'Banana',
        'Price': '1',
        'Quantity': '15',
        'Category': 'Fruit'
    },
    {
        'ItemName': 'Pear',
        'Price': '3',
        'Quantity': '20',
        'Category': 'Fruit'
    },
    {
        'ItemName': 'Cherry',
        'Price': '4',
        'Quantity': '1',
        'Category': 'Fruit'
    }
]


def generate_fixed_width_file(output: str, records: int) -> str:
    """Generates a fixed width file and returns the location of it
    Args:
        output (str): Output folder to generate file into
        records (int): Number of records to generate
    Returns:
        Str: Location of the generated folder
    """
    file_name = os.sep.join(['.', output, 'fixed_width.txt'])
    max_range = len(DATA) - 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(records):
            cur = DATA[randint(0, max_range)]
            for key, padding in SPEC.items():
                file.write(cur[key].ljust(padding, ' '))
            if i != records - 1:
                file.write('\n')

    return file_name


def parse_fixed_width_file(_input: str) -> Generator[dict, None, None]:
    """Parses fixed with file into a csv
    Args:
        output (str): Output folder to generate file into
        _input (str): Input file that contains fixed width data
    
    Yields:
        record (dict): Converted fixed width record
    """
    with open(_input, 'r', encoding='utf-8') as file:
        for file_row in file.readlines():
            position = 0
            record = {}
            for key, padding in SPEC.items():
                end_pos = position+padding
                record[key] = file_row[position:end_pos].strip()
                position = end_pos
            yield record


def main():
    """Main Entry Handler for Function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', type=str, default='output',
                        help='Output folder for generated file and parsed file')
    parser.add_argument('--records', '-r', type=int, default=1000,
                        help='Number of records to generate')

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    fixed_width_file = generate_fixed_width_file(args.output, args.records)
    with open(os.sep.join(['.', args.output, 'output.csv']), 'w', encoding='utf-8') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=SPEC.keys())
        dict_writer.writeheader()
        for record in parse_fixed_width_file(fixed_width_file):
            dict_writer.writerow(record)


if __name__ == "__main__":
    main()
