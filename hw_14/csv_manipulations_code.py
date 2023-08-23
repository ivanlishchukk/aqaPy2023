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


