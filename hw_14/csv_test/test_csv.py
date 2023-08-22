from hw_14.csv_manipulations_code import CSVManipulation


class TestCSV:

    def test_add_row(self):
        csv_file = CSVManipulation()
        csv_file.add_row('example.csv', row_data='Ivan, Lishchuk, age, Male, salary')
        assert csv_file.csv_len('example.csv') == 5

    def test_delete_row(self):
        csv_file = CSVManipulation()
        csv_file.delete_row('example.csv', row_index=3)
        assert csv_file.csv_len('example.csv') == 4