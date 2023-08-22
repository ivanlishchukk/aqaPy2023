import json
import csv

class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def write_file(self, filename: str):
        with open(filename, 'w', newline='') as writer:
            csv_writer = csv.writer(writer)
            if self.__lines:
                header = self.__lines[0]
                csv_writer.writerow(header.keys())
                for value in self.__lines:
                    csv_writer.writerow(value.values())
            self.cleanup()

    def cleanup(self):
        self.__lines = []

converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example.csv')
