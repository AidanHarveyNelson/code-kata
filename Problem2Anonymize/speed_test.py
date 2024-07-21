"""Speed test function to compare small and large parser for Problem 2 Solution"""
import os
import time

from generator import generate_csv_file
from processor import process_small_file, process_large_file

def main():
    output = 'speed_test'
    os.makedirs(output, exist_ok=True)
    record_tests = {
        100: {},
        10000: {},
        1000000: {},
        10000000: {},
        50000000: {},
    }
    for records, value in record_tests.items():
        input_file = generate_csv_file(output, records)
        small_file_name = f'{input_file.split(".", maxsplit=1)[0]}_anon_small.csv'
        split_file_name = f'{input_file.split(".", maxsplit=1)[0]}_anon_large.csv'
        start_time = time.time()
        print('Starting Small file Processing')
        process_small_file(input_file, small_file_name)
        value['small_file_time'] = time.time() - start_time
        start_time = time.time()
        print('Starting Large file Processing')
        process_large_file(input_file, split_file_name)
        value['large_file_time'] = time.time() - start_time

    for key, value in record_tests.items():
        print(f'Test with {key} records:\n'
              f'Small file test took {value["small_file_time"]}s\n'
              f'Large file test took {value["large_file_time"]}s\n')

if __name__ == '__main__':
    main()
