'''
скористайтесь pytest.

напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився.
Y якості перевірного csv можете скористатись доданим до завдання файлом або будь-яким іншим.
'''
import csv


class CSVManipulation:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r', newline='') as csv_reader:
            lines = csv.DictReader(csv_reader)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def csv_len(self, filename):
        with open(filename, 'r') as csv_reader:
            lines = csv_reader.readlines()
        return len(lines)

    def add_row(self, filename: str, row_data):
        with open(filename, 'a') as adder:
            adder.write(f'\n{row_data}')
            adder.close()

    def delete_row(self, filename: str, row_index: int):
        with open(filename, 'r') as csv_reader:
            lines = csv_reader.readlines()
        if 0 < row_index < len(lines):
            del lines[row_index]
            with open(filename, 'w') as csv_writer:
                csv_writer.writelines(lines)
                csv_writer.close()


#csv_file = CSVManipulation()
#csv_file.add_row('example.csv', row_data='Ivan, Lishchuk, age, Male, salary')
#csv_file.delete_row('example.csv', row_index=3)
