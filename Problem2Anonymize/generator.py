"""Helper File to genrate CSV Data"""
from random import randint
import csv
import os


FIELD_NAMES = ['first_name', 'last_name', 'address', 'date_of_birth']


DATA = {
    'first_name': ['bob', 'fred', 'alice', 'frank', 'tim', 'jane'],
    'last_name': ['bean', 'holloway', 'donaldson', 'coleman', 'munoz', 'small'],
    'address': ['3458 Mcwhorter Road', '2704 West Drive', '1328 Ridenour Street',
                '228 McKinley Avenue', '999 Friendship Lane', '123 Parkview Lane'],
    'date_of_birth': ['2003-04-12', '2020-01-05', '1993-03-12',
                        '1998-12-02', '2001-02-13', '2004-10-25']
}


def generate_csv_file(output: str, records: int) -> str:
    """Generates a csv file and returns the location of it
    Args:
        output (str): Output folder to generate file into
        records (int): Number of records to generate
    Returns:
        Str: Location of the generated folder
    """

    file_name = os.sep.join([output, f'users_{records}.csv'])
    with open(file_name, 'w', encoding='utf-8') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        dict_writer.writeheader()

        for _ in range(records):
            dict_writer.writerow({
                'first_name': DATA['first_name'][randint(0, 5)],
                'last_name': DATA['last_name'][randint(0, 5)],
                'address': DATA['address'][randint(0, 5)],
                'date_of_birth': DATA['date_of_birth'][randint(0, 5)],
            })
    return file_name
