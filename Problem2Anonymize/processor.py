"""Main Function For Problem 2 Solution"""
import csv
import hashlib
import multiprocessing as mp
import math
import shutil
from typing import Generator
import os

from generator import FIELD_NAMES


PROTECTED_FIELD_NAMES = ['first_name', 'last_name', 'address']


def get_anonymized_value(data: str) -> str:
    """Anonymized string value
    Args:
        data (str): Data to Anonymize
    Returns:
        Str: Anonymized data
    """
    return hashlib.sha1(data.encode('utf-8')).hexdigest()


def anonymize_csv_file(input_file: str, has_header=True) -> Generator[dict, None, None]:
    """Anonymized CSV file
    Args:
        input_file (str): File to anonymize
    Returns:
        Generator: Each record of file anonymized
    """
    with open(input_file, 'r', encoding='utf-8') as input_csv:
        dict_reader = csv.DictReader(input_csv, fieldnames=FIELD_NAMES)
        if has_header:
            next(dict_reader)
        for record in dict_reader:
            for key, value in record.items():
                record[key] = get_anonymized_value(value) if key in PROTECTED_FIELD_NAMES else value
            yield record


def process_small_file(input_file, output_file, has_header=True):
    """Process small file by processing in sequence using generators
    Args:
        input_file (str): File to anonymize
        output_file (str): File to write result to
    """
    with open(output_file, 'w', encoding='utf-8') as output_csv:
        csv_writer = csv.DictWriter(output_csv, FIELD_NAMES)
        if has_header:
            csv_writer.writeheader()
        for record in anonymize_csv_file(input_file, has_header):
            csv_writer.writerow(record)


def split_file_by_cpu(input_file: str, cpu_count: int) -> list[str]:
    """Split file into smaller parts based on the number of CPU's on host machine
    Args:
        input_file (str): File to anonymize
        cpu_count (int): Number of CPU's on host machine
    Returns:
        list (str): List of file name location for split files
    """
    file_names = []
    num_lines = sum(1 for _ in open(input_file, 'r', encoding='utf-8'))
    def extract_lines(fp, line_numbers):
        return (x for i, x in enumerate(fp) if i >= line_numbers[0] and i < line_numbers[1])
    file_groups = list(range(0, num_lines, math.ceil(num_lines / (cpu_count - 1))))
    for i, line in enumerate(file_groups):
        new_file_name = f'{input_file.split(".")[0]}_{line}.csv'
        with open(new_file_name, 'w', encoding='utf8') as cur_file:
            try:
                next_line = file_groups[i + 1]
            except IndexError:
                next_line = num_lines
            lines = extract_lines(open(input_file, 'r', encoding='utf-8'), [line, next_line])
            cur_file.writelines(lines)
            file_names.append(new_file_name)
    return file_names


def process_large_file(input_file, output_file):
    """Process small file by processing in sequence using generators
    Args:
        input_file (str): File to anonymize
        output_file (str): File to write result to
    """
    cpu_count = mp.cpu_count()
    input_file_names = split_file_by_cpu(input_file, cpu_count)
    args = [(input_file, f'{input_file.split(".", maxsplit=1)[0]}_anon.csv', not bool(i))
                for i, input_file in enumerate(input_file_names)]
    with mp.Pool(processes=cpu_count) as pool:
        pool.starmap(func=process_small_file, iterable=args)

    with open(output_file, 'w', encoding='utf-8') as completed_file:
        for file in args:
            with open(file[1],'r', encoding='utf-8') as cur_file:
                shutil.copyfileobj(cur_file, completed_file)
            os.remove(file[0])
            os.remove(file[1])
